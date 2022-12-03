#include "lists.h"

/**
 * pal_check - reverses the second list for comparison
 * @ptr1: pointer to pointer to list head
 * @ptr2: pointer to last node
 * Return: 0 if it is not palidrome, 1 if it is
 */

int pal_check(listint_t **ptr1, listint_t *ptr2)
{
	if (ptr2 == NULL)
		return (1);

	if (pal_check(ptr1, ptr2->next) && ((*ptr1)->n == ptr2->n))
	{
		*ptr1 = (*ptr1)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks is a singly linked list is a palidrome
 * @head: pointer to pointer to list head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr1 = *head;
	listint_t *ptr2 = *head;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	return (pal_check(&ptr1, ptr2));
}
