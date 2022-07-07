#include <stdio.h>

int main() {
    unsigned short n = 0x0102;

    unsigned char *a = (char*) &n;
    printf("number short: %d\n", n);
    printf("first byte: %d\n", a[0]);
    printf("second byte: %d\n", a[1]);
}
