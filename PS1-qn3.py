import numpy as np

def matToREF(mat, dime):
    for i in range(dime[0]):
        for j in range(dime[1]):
            if(mat[i][j] != 0):
                lead_no = mat[i][j]
                for k in range(dime[1]):
                    mat[i][k] = mat[i][k]/lead_no
                
                if(i+1<dime[0]):
                    
                    for l in range(i+1,dime[0]):
                        mul = mat[l][j]
                        for m in range(j,dime[1]):
                            mat[l][m] = mat[l][m] - mul * mat[i][m]
                print(f"{i}{j} : ",np.matrix(mat))
                break
                
    return mat

def REFtoRREF(ref_mat,dime):
    for i in range(dime[0]):
        for j in range(dime[1]):
            if(ref_mat[i][j] == 1):
                for m in range(i):
                    mul_fac = ref_mat[m][j]
                    for n in range(dime[1]):
                        ref_mat[m][n] = ref_mat[m][n] - mul_fac*ref_mat[i][n]
                break
    return ref_mat


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
        
#np_mat = np.matrix(mat)
print("Entered matrix :")
print(np.matrix(mat))
#rref_mat = REFtoRREF(mat,dime)


#ref_np_mat = np.matrix(rref_mat)

#print("RREF matrix :")
#print(rref_np_mat)

ref_mat = matToREF(mat, dime)
print("REF matrix :")
print(np.matrix(ref_mat))

rref_mat = REFtoRREF(ref_mat,dime)
print("RREF matrix :")
print(np.matrix(rref_mat))