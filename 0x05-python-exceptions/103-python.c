#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about Python lists.
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc;
	Py_ssize_t i;
	PyObject *item;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about Python bytes objects.
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", (size + 1 > 10) ? 10 : size + 1);

	for (i = 0; i < size + 1 && i < 10; i++)
		printf(" %02hhx", str[i]);
	putchar('\n');
}

/**
 * print_python_float - Prints information about Python float objects.
 * @p: PyObject pointer
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	printf("  value: %s\n", Pyos_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

