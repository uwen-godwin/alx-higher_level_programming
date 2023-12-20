#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes:", size + 1);
    for (i = 0; i <= size; ++i)
        printf(" %02x", str[i]);
    printf("\n");
}

/**
 * print_python_float - prints some basic info about Python float objects
 * @p: pointer to PyObject
 */
void print_python_float(PyObject *p)
{
    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

/**
 * print_python_list - prints some basic info about Python list objects
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}

int main(void)
{
    PyObject *p, *l;
    double d;
    char s[60];

    setbuf(stdout, NULL);

    l = PyList_New(0);

    p = PyBytes_FromStringAndSize("Hello", 5);
    print_python_bytes(p);

    PyBytes_DecodeEscape(s, "What does the 'b' character do in front of a string literal?", 60);
    p = PyBytes_FromStringAndSize(s, 60);
    print_python_bytes(p);

    PyList_Insert(l, 0, Py_BuildValue("s", "School"));
    PyList_Append(l, Py_BuildValue("s", "Betty"));
    PyList_SetSlice(l, 0, PyList_Size(l), NULL);

    PyList_Pop(l, PyList_Size(l) - 1);
    
    print_python_list(l);

    return 0;
}
