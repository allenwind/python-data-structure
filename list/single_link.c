/*数组、单链表、双链表

数组：
1、数组的特点是：数据是连续的；随机访问速度快
2、数组中稍微复杂一点的是多维数组和动态数组

单向链表：
1、单向链表(单链表)是链表的一种，它由节点组成，每个节点都包含下一个节点的指针
head-->e1-->e2-->e3

del node
add node

双向链表：
1、双链表也是由节点组成，它的每个数据结点中都有两个指针，分别指向直接后继和直接前驱。
head<-->e1<-->e2<-->e3

del node 
add node
*/
#include <stdio.h>
#include <malloc.h>

//充分利用指针“隔空移物”

//single link node
struct node {
	void * p;
	struct node * next;
}

//the head
static struct node * phead = NULL;

//create node, p is value of node
static struct node * create_node(void * pval) {
	struct node * pnode = NULL;
	pnode = (struct node *) malloc(sizeof(struct node)); //get memory space
	if (!pnode) 
		return NULL;
	pnode->p = pval; //传递的是指针
	pnode->next = NULL;

	return pnode;
}

static void append(void * pval) {
	struct node * pnode = NULL;
	pnode = (struct node *) malloc(sizeof(struct node));
	if (!pnode) {
		printf("can't append pval\n");
		return -1;
	}
	pnode->p = pval;
	pnode->next = NULL;
	

//destroy link from head
static void destroy_single_link() {
	struct node * pnode = NULL;
	while (phead != NULL) {
		pnode = phead;
		phead = phead->next; //把下一个节点设为head
		free(pnode);//释放head的内存
	}
}

//insert pval into link's head
static struct node * push(void * pval) {
	struct node * pnode = NULL;
	pnode = create_node(pval);
	pnode->next = phead;
	phead = pnode 

	return phead;
}

//delete link's head
static void * pop() {
	if (!phead) {
		printf("link is empty\n");
		return -1;
	}

	void * pret;
	struct node * pnode;
	pret = phead->p; //get value of link's head
	pnode = phead;
	phead = phead->next;
	free(pnode);
	return pret; //return value of link's head
}

//get head's value
static void * peek() {
	if (!head) {
		printf("link is empty\n");
		return NULL;
	}
	return phead->p;
}

//get count of node
static int size() {
	int count=0;
	struct node * pnode = phead;
	while (pnode != NULL) {
		pnode = pnode->next;
		count++;
	}
	return count;
}

//print stack








