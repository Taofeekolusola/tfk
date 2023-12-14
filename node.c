#include <stdio.h>
#include <stdlib.h>
#include "struct.h"
int main()
{
	struct node
{
	int salary;
	struct node *next;
};

struct node *nodeA, *nodeB, *nodeC, *nodeD, *nodeAA, *nodeF, *nodeE, *head, *temp;

nodeA = (struct node *)malloc(sizeof(struct node));
nodeB = (struct node *)malloc(sizeof(struct node));
nodeC = (struct node *)malloc(sizeof(struct node));
nodeD = (struct node *)malloc(sizeof(struct node));
nodeAA = (struct node *)malloc(sizeof(struct node));
nodeE = (struct node *)malloc(sizeof(struct node));
nodeF = (struct node *)malloc(sizeof(struct node));

nodeAA->salary = 100000;
nodeAA->next = nodeA;

nodeA->salary = 200000;
nodeA->next = nodeB;

nodeB->salary = 300000;
nodeB->next = nodeC;

nodeC->salary = 400000;
nodeC->next = nodeD;

nodeD->salary = 500000;
nodeD->next = nodeE;

nodeE->salary = 600000;
nodeE->next = nodeF;

nodeF->salary = 700000;
nodeF->next = NULL;

head = nodeAA;
temp = head;

while (temp->next != NULL)
{
	printf("%d---->", temp->salary);
	temp = temp->next;
}
 	printf("%d---->", temp->salary);
 	temp = temp->next;

}
