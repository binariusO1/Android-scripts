import re

dec = 0

def read_file(dec):
    fout = open("output.txt",'w')
    with open("input.txt", 'r') as fin:
        for line in fin.readlines():
            values = line.split()
            for val in values:
                if val.isalpha():
                    new_val = val
                    if val == 'Z':
                        new_val = val + '\n'
                else:
                    f = (float(val))
                    new_val = round(f, dec) # digit precision
                    new_val = str(new_val)

                fout.write(new_val)
                fout.write(' ')
            fout.write('\n')
    fout.close()


#print("Enter decimal place:\n",dec)
dec = int(input("Enter decimal place [0-2]:\n"))
read_file(dec)
print("done")