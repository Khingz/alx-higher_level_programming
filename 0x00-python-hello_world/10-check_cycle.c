#include "lists.h"

/**
 * check_cycle - Checks if a linked list is cycle or not
 * @list:linked list to be checked
 * Return: 1 if cycle or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *turtle;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	turtle = list->next;
	hare = list->next->next;
	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
		{
			return (1);
		}
		turtle = turtle->next;
		hare = hare->next->next;
	}
	return (0);
}
