import re

x = 0
y = 0

def read_file(x,y):
    xy = 0
    fout = open("output_move.txt",'w')
    with open("output.txt", 'r') as fin:
        for line in fin.readlines():
            values = line.split()
            for val in values:
                if val.isalpha():
                    new_val = val
                    if val == 'L' or val == 'Q' or val == 'M':
                        xy=1
                    elif val == 'A':
                        xy = 16
                    else:
                        xy = 0
                else:
                    f = (float(val))
                    if xy == 1:
                        new_val = f + x
                        xy = 2
                    elif xy == 2:
                        new_val = f + y
                        xy = 1
                    elif xy > 12:
                        new_val = f
                        xy = xy -1
                    elif xy == 12:
                        new_val = f
                        xy = 1
                    else:
                        xy = 1
                    new_val = str(new_val)

                fout.write(new_val)
                fout.write(' ')
            fout.write('\n')
    fout.close()


#print("Enter decimal place:\n",dec)
x = int(input("Move X:\n"))
y = int(input("Move Y:\n"))
read_file(x,y)
print("done")