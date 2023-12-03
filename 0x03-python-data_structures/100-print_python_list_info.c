#include <Python.h>

/**
 * print_python_list_info - prints basic info about python lists
 * @p: pointer to a python representing a python a python list
 */
void print_python_list_list(Python *p)
{
	Py_ssize_t, i;
	PyObject_Size(p);

	size = PyList_Size(p);
	printf("[*] size of Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PythonObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\", i, Py_TYPE(item)->tp_name);
	}
}
