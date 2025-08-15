from math import sin,cos,pi
def fft(a):
    n=len(a)
    if n==1:
        return[a[0]]
    theta=-2*pi/n
    w=list(complex(cos(theta*i),sin(theta*i))for i in range(n))
    Aeven=a[0::2]
    Aodd=a[1::2]
    Yeven=fft(Aeven)
    Yodd=fft(Aodd)
    Y=[0]*n
    middle=n//2
    for k in range(n//2):
        w_yodd_k=w[k]*Yodd[k]
        yeven_k=Yeven[k]
        Y[k]        =yeven_k+w_yodd_k
        y[k+middle] = yeven_k-w_yodd_k 
        return Y
#Driver code 
if __name__='__main__':
a=[1,2,3,4]
b=fft(a)
for B in b:
    print(B)




