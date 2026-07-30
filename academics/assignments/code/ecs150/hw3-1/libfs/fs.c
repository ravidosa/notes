#include <assert.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <disk.h>
#include <fs.h>

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

static struct superblock sblock;
static uint16_t *fat = NULL;
static struct dir_entry root_dir[FS_FILE_MAX_COUNT];
static int mounted = 0;

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
