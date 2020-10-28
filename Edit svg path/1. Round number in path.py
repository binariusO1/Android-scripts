import re

dec = 0

def read_file(dec):
    fout = open("output.txt",'w')
    with open("input.txt", 'r') as fin:
        for A in fin.readlines():
            for i in range(len(A)):
                if A[i].isalpha():
                    new_val = A[i]
                    if A[i] == 'Z' or A[i] == 'z':
                        new_val = A[i] + '\n'
                elif A[i] == '.' and A[i+1].isdigit() and A[i+2].isdigit() and A[i+3].isdigit():
                    temp = A[i] + A[i+1]+A[i+2]+A[i+3]
                    f = (float(temp))
                    new_val = round(f, dec) # digit precision
                    if dec==2:
                        new_val = str(new_val)[1] + str(new_val)[2]+str(new_val)[3]
                    elif dec == 1:
                        new_val = str(new_val)[1] + str(new_val)[2]
                elif A[i] == '\n':
                    new_val = '\n'
                elif (A[i-1]=='.' or (A[i-2]=='.' and A[i-1].isdigit()) or (A[i-3]=='.' and A[i-2].isdigit() and A[i-1].isdigit())) and A[i].isdigit():
                    continue
                else:
                    new_val = A[i]
                #print(A[i], i)
                fout.write(new_val)
                #fout.write(' ')
        fout.write('\n')
    fout.close()


#print("Enter decimal place:\n",dec)
dec = int(input("Enter decimal place [1-2]:\n"))

read_file(dec)
print("done")