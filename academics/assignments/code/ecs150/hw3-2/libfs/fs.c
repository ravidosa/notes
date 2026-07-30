#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "disk.h"
#include "fs.h"

#define FS_SIGNATURE "ECS150FS"
#define FAT_EOC 0xFFFF

struct __attribute__((packed)) superblock {
    uint8_t signature[8];
    uint16_t block_ct;
    uint16_t root_block_index;
    uint16_t data_block_index;
    uint16_t data_block_ct;
    uint8_t fat_block_ct;
    uint8_t padding[4079];
};

struct __attribute__((packed)) dir_entry {
    uint8_t filename[16];
    uint32_t file_size;
    uint16_t data_block_index;
    uint8_t padding[10];
};

struct file_descriptor {
    int used;
    int dir_entry;
    size_t offset;
};

static struct superblock sblock;
static uint16_t *fat = NULL;
static struct dir_entry root_dir[FS_FILE_MAX_COUNT];
static int mounted = 0;
static struct file_descriptor fd_table[FS_OPEN_MAX_COUNT];

/* find entry for given filename */
int find_file(const char *filename)
{
    int entry = -1;
    for (int i = 0; i < FS_FILE_MAX_COUNT; i++) {
        if (strncmp((char *)root_dir[i].filename, filename, FS_FILENAME_LEN) ==
            0) {
            entry = i;
            break;
        }
    }
    return entry;
}

/* find data block for given file and offset */
static int find_data_block(int dir_entry, size_t offset)
{
    uint16_t block_index = root_dir[dir_entry].data_block_index;
    size_t block_num = offset / BLOCK_SIZE;

    for (size_t i = 0; i < block_num; i++) {
        if (block_index == FAT_EOC || block_index == 0) {
            return -1;
        }
        block_index = fat[block_index];
    }

    if (block_index == FAT_EOC || block_index == 0) {
        return -1;
    }
    return block_index;
}

/* write FAT to disk */
static int write_FAT(void)
{
    uint8_t buffer[BLOCK_SIZE];
    size_t fat_bytes = (size_t)sblock.data_block_ct * sizeof(uint16_t);
    size_t written_bytes = 0;
    for (int i = 0; i < sblock.fat_block_ct; i++) {
        memset(buffer, 0, BLOCK_SIZE);
        size_t copy_bytes = fat_bytes - written_bytes;
        if (copy_bytes > BLOCK_SIZE) {
            copy_bytes = BLOCK_SIZE;
        }
        memcpy(buffer, (uint8_t *)fat + written_bytes, copy_bytes);
        if (block_write(1 + i, buffer) == -1) {
            return -1;
        }
        written_bytes += copy_bytes;
    }
    return 0;
}

static int extend_file(int dir_entry)
{
    /* allocate new block */
    int new_block = -1;
    for (int i = 0; i < sblock.data_block_ct; i++) {
        if (fat[i] == 0) {
            fat[i] = FAT_EOC;
            new_block = i;
            break;
        }
    }
    if (new_block == -1) {
        return -1;
    }

    /* no blocks in file */
    if (root_dir[dir_entry].data_block_index == FAT_EOC) {
        root_dir[dir_entry].data_block_index = new_block;
    }
    /* traverse until reach end of file */
    else {
        uint16_t block_index = root_dir[dir_entry].data_block_index;
        while (fat[block_index] != FAT_EOC) {
            block_index = fat[block_index];
        }
        fat[block_index] = new_block;
    }
    return new_block;
}

int fs_mount(const char *diskname)
{
    /* oper virtual disk file */
    if (block_disk_open(diskname) == -1) {
        return -1;
    }

    /* read superblock */
    if (block_read(0, &sblock) == -1) {
        block_disk_close();
        return -1;
    }

    /* validate signature (==ECS150FS?) */
    if (memcmp(sblock.signature, FS_SIGNATURE, 8) != 0) {
        block_disk_close();
        return -1;
    }

    /* validate block count */
    if (sblock.block_ct != (uint16_t)block_disk_count()) {
        block_disk_close();
        return -1;
    }

    /* allocate FAT */
    size_t fat_bytes = (size_t)sblock.data_block_ct * sizeof(uint16_t);
    fat = malloc(fat_bytes);
    if (fat == NULL) {
        block_disk_close();
        return -1;
    }

    /* read FAT */
    uint8_t buffer[BLOCK_SIZE];
    size_t read_bytes = 0;
    for (int i = 0; i < sblock.fat_block_ct; i++) {
        if (block_read(1 + i, buffer) == -1) {
            free(fat);
            fat = NULL;
            block_disk_close();
            return -1;
        }
        size_t copy_bytes = fat_bytes - read_bytes;
        if (copy_bytes > BLOCK_SIZE) {
            copy_bytes = BLOCK_SIZE;
        }
        memcpy((uint8_t *)fat + read_bytes, buffer, copy_bytes);
        read_bytes += copy_bytes;
    }

    /* read root dir */
    if (block_read(sblock.root_block_index, root_dir) == -1) {
        free(fat);
        fat = NULL;
        block_disk_close();
        return -1;
    }

    mounted = 1;
    return 0;
}

int fs_umount(void)
{
    if (!mounted) {
        return -1;
    }

    free(fat);
    fat = NULL;

    if (block_disk_close() == -1) {
        return -1;
    }

    mounted = 0;
    return 0;
}

int fs_info(void)
{

    /* count free data blocks in FAT */
    int fat_free = 0;
    for (int i = 0; i < sblock.data_block_ct; i++) {
        if (fat[i] == 0) {
            fat_free++;
        }
    }

    /* count free entries in root directory */
    int rdir_free = 0;
    for (int i = 0; i < FS_FILE_MAX_COUNT; i++) {
        if (root_dir[i].filename[0] == '\0') {
            rdir_free++;
        }
    }

    printf("FS Info:\n");
    printf("total_blk_count=%d\n", sblock.block_ct);
    printf("fat_blk_count=%d\n", sblock.fat_block_ct);
    printf("rdir_blk=%d\n", sblock.root_block_index);
    printf("data_blk=%d\n", sblock.data_block_index);
    printf("data_blk_count=%d\n", sblock.data_block_ct);
    printf("fat_free_ratio=%d/%d\n", fat_free, sblock.data_block_ct);
    printf("rdir_free_ratio=%d/%d\n", rdir_free, FS_FILE_MAX_COUNT);
    return 0;
}

int fs_create(const char *filename)
{
    if (!mounted) {
        return -1;
    }

    if (filename == NULL) {
        return -1;
    }

    if (strlen(filename) == 0 || strlen(filename) >= FS_FILENAME_LEN) {
        return -1;
    }

    /* check if filename already exists */
    if (find_file(filename) != -1) {
        return -1;
    }

    /* find first free entry */
    int free_entry = -1;
    for (int i = 0; i < FS_FILE_MAX_COUNT; i++) {
        if (root_dir[i].filename[0] == '\0') {
            free_entry = i;
            break;
        }
    }
    if (free_entry == -1) {
        return -1;
    }

    /* create empty file in root directory at free_entry */
    memset(&root_dir[free_entry], 0, sizeof(struct dir_entry));
    strncpy((char *)root_dir[free_entry].filename, filename, FS_FILENAME_LEN);
    root_dir[free_entry].file_size = 0;
    root_dir[free_entry].data_block_index = FAT_EOC;

    /* write root directory to disk */
    if (block_write(sblock.root_block_index, root_dir) == -1) {
        return -1;
    }

    return 0;
}

int fs_delete(const char *filename)
{
    if (!mounted) {
        return -1;
    }

    if (filename == NULL) {
        return -1;
    }

    if (strlen(filename) == 0) {
        return -1;
    }

    /* find filename */
    int del_entry = find_file(filename);
    if (del_entry == -1) {
        return -1;
    }

    /* free data blocks in FAT */
    uint16_t block_index = root_dir[del_entry].data_block_index;
    while (block_index != FAT_EOC && block_index != 0) {
        uint16_t next_block_index = fat[block_index];
        fat[block_index] = 0;
        block_index = next_block_index;
    }

    /* write FAT to disk */
    write_FAT();

    /* free directory entry */
    memset(&root_dir[del_entry], 0, sizeof(struct dir_entry));

    /* write root directory to disk */
    if (block_write(sblock.root_block_index, root_dir) == -1) {
        return -1;
    }

    return 0;
}

int fs_ls(void)
{
    if (!mounted) {
        return -1;
    }

    printf("FS Ls:\n");
    for (int i = 0; i < FS_FILE_MAX_COUNT; i++) {
        if (root_dir[i].filename[0] != '\0') {
            printf("file: %s, size: %d, data_blk: %d\n", root_dir[i].filename,
                   root_dir[i].file_size, root_dir[i].data_block_index);
        }
    }
    return 0;
}

int fs_open(const char *filename)
{
    if (!mounted) {
        return -1;
    }

    if (filename == NULL) {
        return -1;
    }

    if (strlen(filename) == 0) {
        return -1;
    }

    /* find filename */
    int open_entry = find_file(filename);
    if (open_entry == -1) {
        return -1;
    }

    /* find first open fd */
    int fd = -1;
    for (int i = 0; i < FS_OPEN_MAX_COUNT; i++) {
        if (!fd_table[i].used) {
            fd = i;
            break;
        }
    }
    if (fd == -1) {
        return -1;
    }

    /* set fd */
    fd_table[fd].used = 1;
    fd_table[fd].dir_entry = open_entry;
    fd_table[fd].offset = 0;

    return fd;
}

int fs_close(int fd)
{
    if (!mounted) {
        return -1;
    }

    if (fd < 0 || fd >= FS_OPEN_MAX_COUNT) {
        return -1;
    }

    if (!fd_table[fd].used) {
        return -1;
    }

    /* unset fd */
    fd_table[fd].used = 0;
    fd_table[fd].dir_entry = -1;
    fd_table[fd].offset = 0;

    return 0;
}

int fs_stat(int fd)
{
    if (!mounted) {
        return -1;
    }

    if (fd < 0 || fd >= FS_OPEN_MAX_COUNT) {
        return -1;
    }

    if (!fd_table[fd].used) {
        return -1;
    }

    return root_dir[fd_table[fd].dir_entry].file_size;
}

int fs_lseek(int fd, size_t offset)
{
    if (!mounted) {
        return -1;
    }

    if (fd < 0 || fd >= FS_OPEN_MAX_COUNT) {
        return -1;
    }

    if (!fd_table[fd].used) {
        return -1;
    }

    if (offset > fs_stat(fd)) {
        return -1;
    }

    fd_table[fd].offset = offset;

    return 0;
}

int fs_write(int fd, void *buf, size_t count)
{
    if (!mounted) {
        return -1;
    }

    if (fd < 0 || fd >= FS_OPEN_MAX_COUNT) {
        return -1;
    }

    if (!fd_table[fd].used) {
        return -1;
    }

    if (buf == NULL) {
        return -1;
    }

    int dir_entry = fd_table[fd].dir_entry;
    size_t offset = fd_table[fd].offset;

    uint8_t bounce[BLOCK_SIZE];
    size_t written_bytes = 0;
    while (written_bytes < count) {
        size_t block_offset = offset % BLOCK_SIZE;
        size_t copy_bytes = BLOCK_SIZE - block_offset;
        if (copy_bytes > count - written_bytes) {
            copy_bytes = count - written_bytes;
        }

        int block_index = find_data_block(dir_entry, offset);
        if (block_index == -1) {
            block_index = extend_file(dir_entry);
            if (block_index == -1) {
                break;
            }
        }

        size_t disk_block_index = sblock.data_block_index + block_index;
        /* partial write */
        if (block_offset != 0 || copy_bytes != BLOCK_SIZE) {
            if (block_read(disk_block_index, bounce) == -1) {
                break;
            }
        } else {
            memset(bounce, 0, BLOCK_SIZE);
        }

        memcpy(bounce + block_offset, (uint8_t *)buf + written_bytes,
               copy_bytes);

        if (block_write(disk_block_index, bounce) == -1) {
            break;
        }

        written_bytes += copy_bytes;
        offset += copy_bytes;
    }

    /* update file size */
    if (offset > root_dir[dir_entry].file_size) {
        root_dir[dir_entry].file_size = offset;
    }

    /* write FAT and root directory to disk */
    write_FAT();
    if (block_write(sblock.root_block_index, root_dir) == -1) {
        return -1;
    }

    fd_table[fd].offset += written_bytes;
    return written_bytes;
}

int fs_read(int fd, void *buf, size_t count)
{
    if (!mounted) {
        return -1;
    }

    if (fd < 0 || fd >= FS_OPEN_MAX_COUNT) {
        return -1;
    }

    if (!fd_table[fd].used) {
        return -1;
    }

    if (buf == NULL) {
        return -1;
    }

    int dir_entry = fd_table[fd].dir_entry;
    size_t offset = fd_table[fd].offset;
    size_t file_size = root_dir[dir_entry].file_size;

    /* bound count to readable bytes */
    if (offset >= file_size) {
        return 0;
    } else if (offset + count > file_size) {
        count = file_size - offset;
    }

    uint8_t bounce[BLOCK_SIZE];
    size_t read_bytes = 0;
    while (read_bytes < count) {
        int block_index = find_data_block(dir_entry, offset);
        if (block_index == -1) {
            break;
        }

        size_t disk_block_index = sblock.data_block_index + block_index;
        if (block_read(disk_block_index, bounce) == -1) {
            break;
        }

        size_t block_offset = offset % BLOCK_SIZE;
        size_t copy_bytes = BLOCK_SIZE - block_offset;
        if (copy_bytes > count - read_bytes) {
            copy_bytes = count - read_bytes;
        }

        memcpy((uint8_t *)buf + read_bytes, bounce + block_offset, copy_bytes);
        read_bytes += copy_bytes;
        offset += copy_bytes;
    }

    fd_table[fd].offset += read_bytes;
    return read_bytes;
}
