#include <stdio.h>
#include <stdlib.h>

struct node {
    struct node * next;
    int value;
};

void reverse(struct node ** list){
    
    struct node * iterator = *list, * lastIt = NULL;
    
    while(iterator != NULL){
        struct node * next = iterator->next;
        
        iterator->next = lastIt;
        lastIt = iterator;

        iterator = next;
        
    }
    
    (*list) = lastIt;
}

int main() {
    struct node * list = calloc(5, sizeof(struct node));
    
    list[4].value = 5;
    list[4].next = NULL;
    list[3].value = 4;
    list[3].next = &list[4];
    list[2].value = 3;
    list[2].next = &list[3];
    list[1].value = 2;
    list[1].next = &list[2];
    list[0].value = 1;
    list[0].next = &list[1];
    
    struct node * iterator = list;
    while(iterator != NULL){ // should see 1 2 3 4 5
        printf("%d ", iterator->value);
        iterator = iterator->next;
    }
    puts("");
    
    reverse(&list);
    
    iterator = list;
    while(iterator != NULL){ // should see 5 4 3 2 1
        printf("%d ", iterator->value);
        iterator = iterator->next;
    }
    puts("");
}
