## interview te aschilo 
def shortest_period(n,sales,k):
       left=0 
       current_sum=0 
       min_length=float('inf')
       for right in range(n):
              current_sum += sales[right]
              ## if sum > k ,window choto korba 
              while current_sum > k :
                     min_length=min(min_length,right-left+1)
                     current_sum -= sales[left]
                     left=left+1

                     return -1 if min_length == float('inf') else min_length
sales=[2,1,5,1,3,2]
k=7 
print(shortest_period(len(sales),sales,k))       

       
       