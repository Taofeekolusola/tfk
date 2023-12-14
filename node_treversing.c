newnode-next = head
head = newnode

temp = head
while (temp->next != NULL)
{
	temp = temp->next
}
temp->next = newnode

temp = head
int i = 1;

while (i < pos)
{
	temp = temp->next
}
i++
newnode->next = temp->next
temp->next = newnode
