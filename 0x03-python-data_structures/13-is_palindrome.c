#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to a pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head;
    listint_t *slow = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    if (fast != NULL)
        slow = slow->next;

    while (slow != NULL)
    {
        if (slow->n != prev->n)
            return 0;
        slow = slow->next;
        prev = prev->next;
    }

    return 1;
}

int main(void)
{
    listint_t *head = NULL;
    listint_t *node1 = malloc(sizeof(listint_t));
    listint_t *node2 = malloc(sizeof(listint_t));
    listint_t *node3 = malloc(sizeof(listint_t));
    listint_t *node4 = malloc(sizeof(listint_t));
    listint_t *node5 = malloc(sizeof(listint_t));

    node1->n = 1;
    node2->n = 2;
    node3->n = 3;
    node4->n = 2;
    node5->n = 1;

    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;
    node5->next = NULL;

    head = node1;

    if (is_palindrome(&head))
        printf("Linked list is a palindrome.\n");
    else
        printf("Linked list is not a palindrome.\n");

    return 0;
}

