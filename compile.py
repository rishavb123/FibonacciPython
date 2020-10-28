import sys

if len(sys.argv) < 2:
    raise Exception('Please pass in a file name')

filename = sys.argv[1]
if filename.split('.')[-1] != 'fpy':
    raise Exception('File must have the .fpy extension')

with open(filename, 'r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        leading_spaces = len(line) - len(line.lstrip(' '))
        if leading_spaces == 0:
            new_lines.append(line)
        elif leading_spaces == 1:
            new_lines.append("   " + line)
        else:
            x = 1
            y = 1
            z = x + y
            c = 2
            while z != leading_spaces:
                if z > leading_spaces:
                    raise Exception('Indentation Error: all indents must have spaces equal to a value in the fibbonacci sequence')
                c += 1
                x = y
                y = z
                z = x + y
            new_lines.append(" " * (c * 4) + line.lstrip(' '))
    with open('.'.join(filename.split('.')[:-1]) + '.py', 'w') as fw:
        fw.writelines(new_lines)