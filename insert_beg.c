#include <stdio.h>
#include <stdlib.h>
#include "struct.h"

void insert_begin(struct node **head, int val)
{
	//create a new node

	struct node *newnode;

	newnode = (struct node *)malloc(sizeof(struct node));

	if (newnode == NULL)
	{
		return;
	}

	newnode->salary = val;

	//check if head is not equal to NULL

	if (*head == NULL) //check if list is empty
	{
		newnode->next = NULL;
	}
	
	else
	{

	//point the next of the newnode to what head was pointing

	newnode->next = *head;
	}

	//make head poit to newnode

	*head = newnode;

	printf("i have successfully added a new node to the begining of the list\n");
}
