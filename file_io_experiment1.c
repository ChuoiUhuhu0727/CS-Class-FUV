#include <stdio.h>

int main() {
    FILE *file = fopen("example.c", "r");
    if (file == NULL) {
        printf("Errors when opening file");
        return 1;
    }

    fclose(file);
    
    file = fopen("example.c", "r+");
    if (file != NULL) {
        fputs("Hello Giang \n", file);
        fclose(file);
    } else {
        printf("Errors opening file ");
    }

    file = fopen("example.c", "r");
    char buffer[101];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }
    
    fclose(file);
    return 0;
}