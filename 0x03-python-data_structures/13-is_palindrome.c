#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head list
 * Return: 1 if the list is ture, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int i = 0;
	int *p;
	listint_t *curr;
	listint_t *end;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	curr = *head;
	while (curr != NULL)
	{
		len++;
		curr = curr->next;
	}

	p = malloc(sizeof(int) * len);
	if (p == NULL)
		return (0);

	curr = *head;
	while (curr != NULL)
	{
		p[i] = curr->n;
		curr = curr->next;
		i++;
	}
	
	end = *head;
	for (i = 0; i < len / 2; i++)
	{
		if (p[i] != end->n)
		{
			free(p);
			return (0);
		}
		end = end->next;
	}
	free(p);
	return (1);
}
