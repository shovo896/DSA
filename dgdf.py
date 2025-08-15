struct node * head ;
struct node * one = Null ;
struct node * two = Null ;
struct node * three = Null ;

one = malloc(sizeof(struct node));
two = malloc(sizeof(struct node));
three = malloc(sizeof(struct node));
one -> data = 1 ;
two -> data= 2 ;
three -> data = 3 ;
one -> next = two ;
two -> next = three ;
three -> next = Null ;
head = one ;