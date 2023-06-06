#include "lists.h"
/**
 * check_cycle - checks if linked list include a cycle
 * @list: linked list to beb checked
 * Return: 1 if cycle exist ,0 if doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
