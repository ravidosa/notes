tm_file = input()
input_alph = input()

sigma = []
transition = {}
delta = False

for line in open(tm_file, "r").readlines():
    line = line.strip()
    if not delta:
        if line.startswith("states"):
            states = line[line.index("{") + 1:line.index("}")].split(",")
        elif line.startswith("input_alphabet"):
            sigma_inp = line[line.index("{") + 1:line.index("}")].split(",")
        elif line.startswith("tape_alphabet_extra"):
            sigma_tape = line[line.index("{") + 1:line.index("}")].split(",")
        elif line.startswith("start_state"):
            start = line[line.index("=") + 1:].strip()
        elif line.startswith("accept_state"):
            accept = line[line.index("=") + 1:].strip()
        elif line.startswith("reject_state"):
            reject = line[line.index("=") + 1:].strip()
        elif line.startswith("num_tapes"):
            tapes = int(line[line.index("=") + 1:])
        elif line.startswith("delta"):
            delta = True
    elif delta:
        si, read, sf, write, move = line.replace(";", "").replace(" -> ", ",").split(",")
        transition[(si, read)] = (sf, write, move)

sigma = sigma_inp + sigma_tape

with open(tm_file[:tm_file.index(".")] + ".tds", "w") as f:
    for alph in sigma_inp:
        f.write(f"""
TILENAME INPUT_{alph}
LABEL [{start}],{alph}
NORTHBIND 2
NORTHLABEL [{start}],{alph}
EASTBIND 2
EASTLABEL 1
TILECOLOR #00ff00
CREATE
""")
    f.write(f"""
TILENAME INPUT1
LABEL _
NORTHBIND 1
NORTHLABEL _
EASTBIND 2
EASTLABEL 2
WESTBIND 2
WESTLABEL 1
TILECOLOR #ffffff
CREATE

TILENAME INPUT2
LABEL _
NORTHBIND 1
NORTHLABEL _*
WESTBIND 2
WESTLABEL 2
TILECOLOR #ffffff
CREATE
""")
    f.write(f"""
TILENAME RIGHT0
LABEL _
NORTHBIND 1
NORTHLABEL _*
WESTBIND 1
WESTLABEL >
TILECOLOR #ffffff
CREATE

TILENAME RIGHT1
LABEL _
NORTHBIND 1
NORTHLABEL _
EASTBIND 2
EASTLABEL _*
SOUTHBIND 1
SOUTHLABEL _*
WESTBIND 1
WESTLABEL >
TILECOLOR #ffffff
CREATE

TILENAME RIGHT2
LABEL _
NORTHBIND 1
NORTHLABEL _*
WESTBIND 2
WESTLABEL _*
TILECOLOR #ffffff
CREATE
            
TILENAME [{accept}],1
LABEL {accept}
SOUTHBIND 2
SOUTHLABEL [{accept}],1
TILECOLOR #ff0000
CREATE 
""")
    for alph in sigma:
        if alph in sigma_inp:
            f.write(f"""
TILENAME [{start}],{alph}
LABEL [{start}],{alph}
NORTHBIND 2
NORTHLABEL [{start}],{alph}
EASTBIND 1
EASTLABEL >
TILECOLOR #{hex(int((ord(alph) - 97) / 26 * 16 ** 6 - 1))[2:]}
CREATE
""")
        f.write(f"""
TILENAME {alph}|<|{alph}|<
LABEL {alph}
NORTHBIND 1
NORTHLABEL {alph}
EASTBIND 1
EASTLABEL <
SOUTHBIND 1
SOUTHLABEL {alph}
WESTBIND 1
WESTLABEL <
TILECOLOR #{"ffffff" if alph in "#_" else hex(int(int(alph) / 4 * 16 ** 2))[2:] * 3 if alph in "0123" else hex(int((ord(alph) - 97) / 26 * 16 ** 6 - 1))[2:]}
CREATE
""")
        if alph in sigma_tape:
            f.write(f"""
TILENAME {alph}|>|{alph}|>
LABEL {alph}
NORTHBIND 1
NORTHLABEL {alph}
EASTBIND 1
EASTLABEL >
SOUTHBIND 1
SOUTHLABEL {alph}
WESTBIND 1
WESTLABEL >
TILECOLOR #{"ffffff" if alph in "#_" else hex(int(int(alph) / 4 * 16 ** 2))[2:] * 3}
CREATE
""")
    for tr in transition:
        si, read = tr
        sf, write, move = transition[tr]
        if move == "R":
            f.write(f"""
TILENAME {write}|[{si}],{read}|[{si}],{read}|<
LABEL {write}
NORTHBIND 1
NORTHLABEL {write}
EASTBIND 1
EASTLABEL [{si}],{read}
SOUTHBIND 2
SOUTHLABEL [{si}],{read}
WESTBIND 1
WESTLABEL <
TILECOLOR #{"ffffff" if write in "#_" else hex(int(int(write) / 4 * 16 ** 2))[2:] * 3 if write in "0123" else hex(int((ord(write) - 97) / 26 * 16 ** 6 - 1))[2:]}
CREATE
""")
            if si == "read" and sf == "right":
                f.write(f"""
TILENAME [{sf}],#|>|#|[{si}],{read}
LABEL [{sf}],#
NORTHBIND 2
NORTHLABEL [{sf}],#
EASTBIND 1
EASTLABEL >
SOUTHBIND 1
SOUTHLABEL #
WESTBIND 1
WESTLABEL [{si}],{read}
TILECOLOR #{"ffffff" if alph in "#_" else hex(int(int(alph) / 4 * 16 ** 2))[2:] * 3 if alph in "0123" else hex(int((ord(alph) - 97) / 26 * 16 ** 6 - 1))[2:]}
CREATE
""")
            else:
                for alph in (sigma if si in ["read", "init", "repeat", "cleanup"] else sigma_tape):
                    f.write(f"""
TILENAME [{sf}],{alph}|>|{alph}|[{si}],{read}
LABEL [{sf}],{alph}
NORTHBIND 2
NORTHLABEL [{sf}],{alph}
EASTBIND 1
EASTLABEL >
SOUTHBIND 1
SOUTHLABEL {alph}
WESTBIND 1
WESTLABEL [{si}],{read}
TILECOLOR #{"ffffff" if alph in "#_" else hex(int(int(alph) / 4 * 16 ** 2))[2:] * 3 if alph in "0123" else hex(int((ord(alph) - 97) / 26 * 16 ** 6 - 1))[2:]}
CREATE
""")
        elif move == "L":
            f.write(f"""
TILENAME {write}|<|[{si}],{read}|[{si}],{read}
LABEL {write}
NORTHBIND 1
NORTHLABEL {write}
EASTBIND 1
EASTLABEL >
SOUTHBIND 2
SOUTHLABEL [{si}],{read}
WESTBIND 1
WESTLABEL [{si}],{read}
TILECOLOR #{"ffffff" if write in "#_" else hex(int(int(write) / 4 * 16 ** 2))[2:] * 3 if write in "0123" else hex(int((ord(write) - 97) / 26 * 16 ** 6 - 1))[2:]}
CREATE
""")
            if si == "read" and sf == "right":
                alph = chr(ord(read) - 1)
                f.write(f"""
TILENAME [{sf}],#|[{si}],{read}|#|<
LABEL [{sf}],#
NORTHBIND 2
NORTHLABEL [{sf}],#
EASTBIND 1
EASTLABEL #
SOUTHBIND 1
SOUTHLABEL <
WESTBIND 1
WESTLABEL [{si}],{read}
TILECOLOR #{"ffffff" if alph in "#_" else hex(int(int(alph) / 4 * 16 ** 2))[2:] * 3 if alph in "0123" else hex(int((ord(alph) - 97) / 26 * 16 ** 6 - 1))[2:]}
CREATE
""")
            else:
                for alph in (sigma if si in ["read", "init", "repeat", "cleanup"] else sigma_tape):
                    f.write(f"""
TILENAME [{sf}],{alph}|[{si}],{read}|{alph}|<
LABEL [{sf}],{alph}
NORTHBIND 2
NORTHLABEL [{sf}],{alph}
EASTBIND 1
EASTLABEL [{si}],{read}
SOUTHBIND 1
SOUTHLABEL {alph}
WESTBIND 1
WESTLABEL <
TILECOLOR #{"ffffff" if alph in "#_" else hex(int(int(alph) / 4 * 16 ** 2))[2:] * 3 if alph in "0123" else hex(int((ord(alph) - 97) / 26 * 16 ** 6 - 1))[2:]}
CREATE
""")
        elif move == "S":
            f.write(f"""
TILENAME [{sf}],{write}|<|[{si}],{read}|>
LABEL {write}
NORTHBIND 2
NORTHLABEL [{sf}],{write}
EASTBIND 1
EASTLABEL >
SOUTHBIND 2
SOUTHLABEL [{si}],{read}
WESTBIND 1
WESTLABEL <
TILECOLOR #{"ffffff" if write in "#_" else hex(int(int(write) / 4 * 16 ** 2))[2:] * 3 if write in "0123" else hex(int((ord(write) - 97) / 26 * 16 ** 6 - 1))[2:]}
CREATE
""")
with open(tm_file[:tm_file.index(".")] + ".tdp", "w") as f:
    f.write(f"""
{tm_file[:tm_file.index(".")]}.tds
temperature=2
INPUT_{input_alph} 0 0
""")