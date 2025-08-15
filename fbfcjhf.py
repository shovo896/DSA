class MinStack {
    public : 
       typedef  struct node {
           int v ;
           int minUntiNow;
           node * next ;
       } node ;
       MinStack : topN(nullptr) {
           
       }
    void push (int val) {
        node * n = new node ;
        n -> v = n -> minUntiNow = val ; 
        n-> next = nullptr ; 
        if (topN == nullptr) {
            topN = n ;
        }
        else {
            n-> minUntiNow =min(n->,topN-> minUntilNow);
            n-> next = topN ;
            topN = n ;
        }
    }
    void pop () {
        topN = topN-> next ;
    }
    int top() {
        return topN -> v ;
    }
    int getMin() {
        return topN -> minUnitilNow;
    }
    private :
    node * topN ; 
};  
