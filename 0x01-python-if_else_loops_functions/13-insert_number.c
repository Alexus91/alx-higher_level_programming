#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - number into a sorted singly linked list.
 * @head: Pointer to the head.
 * @number: Number to be inserted.
 *
 * Return: The address of the new node, if failed NULL .
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (curr == NULL)
		return (NULL);

	new_node->n = number;


	if (curr == NULL || curr->n >= number)
	{
		new_node->next = curr;
		*head = new_node;
		return (new_node);
	}
	while (curr && curr->next && curr->next->n < number)
	{
		curr = curr->next;
	}

	new_node->next = curr->next;
	curr->next = new_node;
	return (new_node);
}
