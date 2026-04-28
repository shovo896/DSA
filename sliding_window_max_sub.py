def max_num(arr,k):
       window_sum=sum(arr[:k])
       max_sum=window_sum

       for i in range(k,len(arr)):
              window_sum+=arr[i]-arr[i-k]
              max_sum=max(max_sum,window_sum)
              return max_sum
arr=[1,4,2,10,2,3,1, 5]
k=3
print(max_num(arr,k))