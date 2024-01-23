#include <Python.h>
#include <floatobject.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    PyObject *element;
    
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str ? str : "(no print)");

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
        printf("%02hhx", str[i]);
        if (i + 1 < size && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");

    // Accessing CPython internal structure for floats
    double value = ((PyFloatObject *)p)->ob_fval;

    printf("  value: %f\n", value);
}
