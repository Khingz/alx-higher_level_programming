#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, n, mem_alloc;
	PyObject *obj;

	size = Py_SIZE(p);
	mem_alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", mem_alloc);
	n = 0;
	while (n < size)
	{
		printf("Element %d: ", n);
		obj = PyList_GetItem(p, n);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		n++;
	}
}
