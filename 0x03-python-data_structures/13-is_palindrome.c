#include "lists.h"

listint_t *reverse_listint(listint_t **head);
listint_t *copy_listint(listint_t **head);
/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t **rev, **copy;
	listint_t *copy_tmp, *tmp;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	copy_tmp = tmp = NULL;

	rev = malloc(sizeof(listint_t *));
	copy = malloc(sizeof(listint_t *));
	if (rev == NULL || copy == NULL)
	{
		return (0);
	}
	*copy = copy_listint(head);
	*rev = reverse_listint(copy);
	tmp = *head;
	copy_tmp = *rev;
	while (tmp)
	{
		if (tmp->n != copy_tmp->n)
		{
			free_listint(*rev);
			free(rev);
			free(copy);
			return (0);
		}
		tmp = tmp->next;
		copy_tmp = copy_tmp->next;
	}
	free_listint(*rev);
	free(rev);
	free(copy);
	return (1);
}

/**
 * copy_listint - copies a list in memory to another memory
 * @head: head of list to be copied
 * Return: NULL or address of head of coppied list
 */
listint_t *copy_listint(listint_t **head)
{
	listint_t *new_head;
	listint_t *tmp, *item, *prev;

	if (head == NULL || *head == NULL)
	{
		return (NULL);
	}
	new_head = prev = NULL;
	tmp = *head;
	while (tmp)
	{
		item = malloc(sizeof(listint_t));
		if (item == NULL)
			return (NULL);
		item->n = tmp->n;
		item->next = NULL;

		if (new_head == NULL)
		{
			new_head = item;
			prev = item;
		}
		else
		{
			prev->next = item;
			prev = item;
		}
		tmp = tmp->next;
	}
	return (new_head);
}

/**
 * reverse_listint - reverses a singly linked list
 * @head: pointer to the for element
 * Return: pointer to first element of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *next;

	if (head == NULL || *head == NULL)
	{
		return (NULL);
	}
	prev = NULL;
	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = next;
	}
	*head = prev;
	return (*head);
}
