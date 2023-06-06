#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: pointer the head of list.
 * @number: number to insert.
 * Return: return NULL or head of list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new_num;

	if (head == NULL)
		return (NULL);
	temp = *head;
	new_num = malloc(sizeof(listint_t));
	if (new_num == NULL)
		return (NULL);
	new_num->n = number;
	if (temp == NULL || temp->n >= number)
	{
		new_num->next = temp;
		*head = new_num;
		return (new_num);
	}
	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;
	new_num->next = temp->next;
	temp->next = new_num;
	return (new_num);
}
