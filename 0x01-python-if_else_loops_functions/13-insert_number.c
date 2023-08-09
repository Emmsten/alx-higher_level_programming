#include <stdlib.h>

/* Definition of singly linked list node structure */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function to insert a number into a sorted singly linked list */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
    {
        return NULL;  /* Return NULL if memory allocation fails */
    }

    new_node->n = number;

    if (*head == NULL || number < (*head)->n)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        listint_t *current = *head;
        while (current->next != NULL && number > current->next->n)
        {
            current = current->next;
        }
        new_node->next = current->next;
        current->next = new_node;
    }

    return new_node;  /* Return the address of the new node */
}

