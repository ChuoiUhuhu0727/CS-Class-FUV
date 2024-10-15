//Create a program that prompts the user 
//to enter their name and age. 
//Save this data in a file named "data.txt"
// in a formatted way

#include <stdio.h>

int main() {
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        printf("Errors opening file");
        return 1;
    } else {
        //get the input value 
        char name[50];
        int age;
        printf("Enter your name: ");
        scanf("%s", name);
        printf("Enter your age: ");
        scanf("%d", &age);

        //print the input and write to the file
        fprintf(file, "Name is %s\nAge is %d\n", name, age);
        fclose(file);
    }
    
    // reopen and print to check
    file = fopen("data.txt", "r");
    
    char buffer[100];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }
    fclose(file);
    return 0;
}