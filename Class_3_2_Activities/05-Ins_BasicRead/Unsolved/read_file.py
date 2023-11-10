import os
file_path = "05-Ins_BasicRead/Resources/input.txt" #path is not working
#file_path = os.path.join("..", "05-Ins_BasicRead", "input.txt")
with open(file_path) as f:
    lines = f.read()
    print(lines)