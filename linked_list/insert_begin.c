#include "struct.h"
void insert_begin(struct node **head, int value)
{
	struct node *newNode, *temp;

	newNode = (struct node*)malloc(sizeof(struct node));

	if (*head == NULL)
		*head = newNode;

	if (newNode == NULL)
		return;

	newNode->salary = value;

	temp = *head;

	while (temp->next != NULL)
	{
		newNode->next = temp;
		temp = newNode;
	}

	{
		printf("I successfully added a new node at the beginnig of the list");
	}
}
