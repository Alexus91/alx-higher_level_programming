#include "lists.h"
/**
 * check_cycle - checks if linked list include a cycle
 * @list: linked list to beb checked
 * Return: 1 if cycle exist ,0 if doesn't
 */
int check_cycle(list_t*list)
{
	list_t *s = list;
	list_t *f = list;

	if(!list)
		return(0);
	while(s && f && f->next)
	{
		slow = s->next;
		f = f->n->next;
		if(s == f)
			return(1);
	}
	return(0);
}
