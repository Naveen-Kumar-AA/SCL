import numpy as np

def chkREF(mat, dime):
    
    for i in range(dime[0]):
        for j in range(dime[1]):
            if(mat[i][j] == 0):
                continue
            else:
                if(mat[i][j] == 1):
                    if(i<dime[0]-1):
                        for k in range(j):
                            if(mat[i+1][k]!=0):
                                return False
                    break
                else:
                    return False
            
                
    return True

def chkRREF(mat, dime):
    
    for i in range(dime[0]):
        for j in range(dime[1]):
            if(mat[i][j] == 0):
                continue
            else:
                if(mat[i][j] == 1):
                    for k in range(dime[0]):
                        if(mat[k][j] != 0):
                            if(k == i):
                                continue
                            return False
                break

    return True

rows = int(input("Enter the no of rows :"))
columns = int(input("Enter the no of columns :"))

dime = [rows, columns]
mat = []

for i in range(dime[0]):
    temp_mat = []
    for j in range(dime[1]):
        a = int(input(f"A{i}{j} :"))
        temp_mat.append(a)
    mat.append(temp_mat)
        
print("Entered matrix :")
print(np.matrix(mat))

if(chkRREF(mat,dime)):
    print("The given matrix is in RREF!")
else:
    
    if(chkREF(mat,dime)):
        print("The given matrix is in REF!")
    else:
        print("The given matrix is not in REF!")