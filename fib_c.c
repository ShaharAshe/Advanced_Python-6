#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

EXPORT int fib1(int a0, int a1, int n) {
    int i, a_n = 0;
    if (n == 0) {
        return a0;
    } else if (n == 1) {
        return a1;
    } else {
        a_n = a0;
        int b_n = a1;
        for (i = 2; i <= n; i++) {
            int temp = b_n;
            b_n = a_n + b_n;
            a_n = temp;
        }
        return b_n;
    }
}

EXPORT int* fib2(int a0, int a1, int count, int* arr) {
    if (arr == NULL) {
        arr = (int*) malloc(count * sizeof(int));
    }
    arr[0] = a0;
    arr[1] = a1;
    for (int i = 2; i < count; i++) {
        arr[i] = arr[i-1] + arr[i-2];
    }
    return arr;
}