#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: PyObject
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
PyObject *item;
PyListObject *list = (PyListObject *)p;
int k, size, alloc;

size = Py_SIZE(p);
alloc = list->allocated;
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

for (k = 0; k < size; k++)
{
item =  PyList_GetItem(p, k);
printf("Element %d: %s\n", k, Py_TYPE(item)->tp_name);
}
}
