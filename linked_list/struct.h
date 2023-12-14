#ifndef STRUCT_H
#define STRUCT_H

#include <stdio.h>
#include <stdlib.h>

struct node
{
	int salary;
	struct node *next;
};
void insert_begin(struct node **head, int value);
#endif
