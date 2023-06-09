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
	listint_t **copy, *tmp, *tmp_copy;

	if (head == NULL)
		return (1);
	tmp = *head;
	copy = malloc(sizeof(listint_t));
	if (copy == NULL)
	{
		return (0);
	}
	*copy = copy_listint(head);
	*copy = reverse_listint(copy);
	tmp_copy = *copy;
	while (tmp)
	{
		if (tmp->n != tmp_copy->n)
		{
			free_listint(*copy);
			free(copy);
			return (0);
		}
		tmp = tmp->next;
		tmp_copy = tmp_copy->next;
	}
	free_listint(*copy);
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
