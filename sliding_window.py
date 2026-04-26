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

       
       