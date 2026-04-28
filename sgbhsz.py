import math

def copy_matrix(A):
    return float[[float(A[i][j]) for j in range(len(A[0]))] for i in range(len(A))]

def identity_matrix(n):
    I=[]
    for i in range(n):
        row=[]
    for j in range(n):
        row.append(1.0 if i ==j else 0.0 )
    l.append(row)
    return l 


def transpose(A):
    rows=len(A)
    cells =len(A[0])


    T=[]

    for j in range(cols):
        row=[] 
        for i in range(n):
        row.append(A[i][j]) 
        T.append(row)
        return T 
        

def Multiply(A,B) : 
    rows_A=len(A)
    cols_A= len(A[0])
    cols_B=len(B[0])

    c=[]

    for i in range(rows_A):
        row=[]
        for j in range(cols_B): 
            total =0.0 
            for k in range(cols_A):
                total += A[i][j] * B[k][j]
            row.append(total)
        C.append(row)

    return C