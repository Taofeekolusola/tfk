#ifndef HASH_TABLE_MAIN
#define HASH_TABLE_MAIN

typedef struct Ht_item
{
    char* key;
    char* value;
} Ht_item;

typedef struct HashTable
{
    // Contains an array of pointers to items.
    Ht_item** items;
    int size;
    int count;
} HashTable;
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
Ht_item* item = create_item(key, value);
int index = hash_function(key);
Ht_item* create_item(char* key, char* value);
HashTable* create_table(int size);
void free_item(Ht_item* item);
void free_table(HashTable* table);
void print_table(HashTable* table)
#endif
