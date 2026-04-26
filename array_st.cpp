#include<iostream>
#include<vector> 
#include<algorithm>
using namespace std ;
int main(){
       vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
       int count = count_if(arr.begin(), arr.end(), [](int x)
                            { return x % 2 == 0; });

       cout << "Even count : " << count << endl;
       return 0;
}
