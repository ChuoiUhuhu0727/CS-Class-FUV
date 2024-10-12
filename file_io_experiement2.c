/* Exercise: Write a program that opens a text file named "text.txt" 
and reads each character in the file one by one 
until the end of the file is reached. 
Display each character on a new line.*/

#include <stdio.h>
int main() {
    FILE *file = fopen("example.c", "r");
    if (file == NULL) {
        printf("Errors opening file\n");
        return 1;
    } else {
        int ch;
        while ((ch = fgetc(file)) != EOF) {
            printf("%c\n", ch);
        }
    }
    fclose(file);
    return 0;
    }