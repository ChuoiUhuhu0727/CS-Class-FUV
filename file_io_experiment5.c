//Ex5: Implement a program that copies the contents of 
//"source.txt" to "destination.txt". 
//Use functions to read from one file and write to another, 
//reading and writing one character at a time.

#include <stdio.h>

int main() {
    FILE *source = fopen("source.txt", "r");

    FILE *destination = fopen("destination.txt", "w");

    char buffer[100];
    while (fgets(buffer, sizeof(buffer), source) != NULL) {
        fputs(buffer, destination);
    }

    fclose(source);
    fclose(destination);
    return 0;
}

