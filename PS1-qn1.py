import numpy as np

noOfVar = int(input("Enter no of variables :"))
noOfEqn = int(input("Enter no of eqns :"))

aug_mat = []

for i in range(noOfEqn):
    temp_list = []
    for j in range(noOfVar):
        x = int(input(f"Enter the coeff of {j+1} variable :"))
        temp_list.append(x)
    y = int(input("Enter the constant term :"))
    temp_list.append(y)
    aug_mat.append(temp_list)
    

aug = np.matrix(aug_mat)  
print(aug)