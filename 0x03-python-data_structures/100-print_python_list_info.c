#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size;
    Py_ssize_t i;
    PyObject *item;

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

int main(void)
{
    PyObject *list;

    Py_Initialize();
    list = PyList_New(0);
    PyList_Append(list, Py_BuildValue("i", 1));
    PyList_Append(list, Py_BuildValue("i", 2));
    PyList_Append(list, Py_BuildValue("i", 3));
    PyList_Append(list, Py_BuildValue("i", 4));

    print_python_list_info(list);

    return 0;
}

