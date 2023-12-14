#include "struct.h"
int main()
{
struct node *nodeA, *nodeB, *nodeC, *nodeD, *head, *temp;
nodeA = (struct node*)malloc(sizeof(struct node));
nodeB = (struct node*)malloc(sizeof(struct node));
nodeC = (struct node*)malloc(sizeof(struct node));
nodeD = (struct node*)malloc(sizeof(struct node));

nodeA->salary = 1000000;
nodeA->next = nodeB;

nodeB->salary = 1500000;
nodeB->next = nodeC;

nodeC->salary = 2000000;
nodeC->next = nodeD;

nodeD->salary = 2500000;
nodeD->next = NULL;

head = nodeA;
temp = head;

//insert a new node at the beginning
 insert_begin(&head, 3000000);

while (temp != NULL)
{
	printf("%d----->", temp->salary);
		temp = temp->next;
}
}
