#include <stdio.h>


//list
//append
//extend
//insert
//remove
//pop
//index
//count
//copy
//clear
//size
//reverse
//sort

struct node {
	void * p;
	struct node * next;
	struct head * head;
	struct head * end;
}

struct head {
	struct node * next;
}

struct head list() {
	struct node * pnode = NULL;
	struct head 