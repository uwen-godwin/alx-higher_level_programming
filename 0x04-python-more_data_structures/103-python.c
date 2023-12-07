#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: Pointer to a PyObject
 */
void print_python_list(PyObject *p)
{
    int size, alloc, i;
    PyObject *item;

    if (p == NULL || !PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Python List\n");
        return;
    }

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

/**
 * print_python_bytes - Prints some basic info about Python bytes
 * @p: Pointer to a PyObject
 */
void print_python_bytes(PyObject *p)
{
    int size, i;
    char *str;

    if (p == NULL || !PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %d\n", size);
    printf("  trying string: %s\n", str);
    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++)
        printf("%02x ", (unsigned char)str[i]);
    printf("\n");
}
