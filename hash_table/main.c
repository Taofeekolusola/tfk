#include "hash_table.h"
{
// Creates the item.
Ht_item* item = create_item(key, value);

// Computes the index.
int index = hash_function(key);

Ht_item* current_item = table->items[index];

if (current_item == NULL)
{
    // Key does not exist.
    if (table->count == table->size)
    {
        // HashTable is full.
        printf("Insert Error: Hash Table is full\n");
        free_item(item);
        return;
    }

    // Insert directly.
    table->items[index] = item;
    table->count++;
	if (current_item == NULL)
	{
	    return NULL
	}
	else {
    // Scenario 1: Update the value.
    if (strcmp(current_item->key, key) == 0)
    {
        strcpy(table->items[index] -> value, value);
        return;
    }
	
	}
}
}
