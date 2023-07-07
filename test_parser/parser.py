import os
import os.path

# PLEASE READ: The code design for this parser is worse than the DreamBerd source code :D
# (from HaxeFloppa/epok_gamer/dreamberddev. 10:29AM BST Tuesday 4th July 2023)
pour_cmd = ['p', 'o', 'u', 'r']
exit_cmd = ['e', 'x', 'i', 't']
read_cmd = ['r', 'e', 'a', 'd']
sip_cmd = ['s', 'i', 'p']

def main():
    while True:
        print("\n\n")
        print("MILKSCRIPT CLIENT")
        print("twitter rate limits are gonna send us outside")
        print("============================")
        for file in os.listdir():
            if os.path.isdir(file):
                print(f'{file}/')
            else:
                print(file)
        print("============================")
        inp = input("Open a MilkScript file: ")
        compile_file = open(inp, "r").read()
        compile_lines = []
        program_counter = 0
        stack = []
        pour_str = ""
        cmd = ""
        cmd_count = 0
        in_paren = False
        for letter in compile_file:
            compile_lines.append(letter)
        print("\n")
        while program_counter != len(compile_lines):
            if compile_lines[program_counter - 1] == ";" and in_paren == False and program_counter < len(compile_lines) or program_counter == 0:
                cmd_count = program_counter
                while not compile_lines[cmd_count] == "(":
                    cmd += compile_lines[cmd_count]
                    cmd_count += 1
                if cmd == "pour":
                    program_counter += 5
                    in_paren = True
                    while compile_lines[program_counter] != ")":
                        pour_str += compile_lines[program_counter]
                        program_counter += 1
                    in_paren = False
                    stack.append(pour_str)
                    pour_str = ""
                    program_counter += 1
                elif cmd == "exit":
                    cmd = ""
                    cmd_count = 0
                    break
                elif cmd == "read":
                    print(stack[int(compile_lines[program_counter + 1])])
                    program_counter += 3
                elif cmd == "sip":
                    stack.pop(len(stack) - 1)
                    program_counter += 3
                cmd = ""
                cmd_count = 0
                continue
            elif cmd == "pour":
                program_counter += 1
                in_paren = True
                while compile_lines[program_counter] != ")":
                    pour_str += compile_lines[program_counter]
                    program_counter += 1
                in_paren = False
                stack.append(pour_str)
                pour_str = ""
                program_counter += 1
                cmd = ""
                cmd_count = 0
                continue
            elif cmd == "exit":
                cmd = ""
                cmd_count = 0
                break
            elif cmd == "read":
                print(stack[int(compile_lines[program_counter + 1])])
                program_counter += 3
                cmd = ""
                cmd_count = 0
                continue
            elif cmd == "sip":
                stack.pop(len(stack) - 1)
                program_counter += 3
                cmd = ""
                cmd_count = 0
            elif program_counter == len(compile_lines) or program_counter > len(compile_lines):
                break
            else:
                if in_paren:
                    continue
                elif compile_lines[program_counter] == ";":
                    program_counter += 2
                    continue
                elif compile_lines[program_counter - 1] == ";" and in_paren == False or program_counter == 0:
                    cmd_count = program_counter
                    while not compile_lines[cmd_count] == "(":
                        cmd += compile_lines[cmd_count]
                        cmd_count += 1
                    if cmd == "pour":
                        program_counter += 5
                        in_paren = True
                        while compile_lines[program_counter] != ")":
                            pour_str += compile_lines[program_counter]
                            program_counter += 1
                        in_paren = False
                        stack.append(pour_str)
                        pour_str = ""
                        program_counter += 1
                    elif cmd == "exit":
                        cmd = ""
                        cmd_count = 0
                        break
                    elif cmd == "read":
                        print(stack[int(compile_lines[program_counter + 1])])
                        program_counter += 3
                    elif cmd == "sip":
                        stack.pop(len(stack) - 1)
                        program_counter += 3
                    cmd = ""
                    cmd_count = 0
                    continue
                elif compile_lines[program_counter] in pour_cmd or compile_lines[program_counter] in exit_cmd or compile_lines[program_counter] in read_cmd or compile_lines[program_counter] in sip_cmd:
                    cmd += compile_lines[program_counter]
                    program_counter += 1
                    continue                   
                else:
                    print(f'Error at col {program_counter}: {compile_lines[program_counter]} is undefined!')
                    break
            program_counter += 1
        stack.clear()
        compile_lines.clear()
        program_counter = 0

if __name__ == '__main__':
    main()
