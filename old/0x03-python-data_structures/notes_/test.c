#include <stdio.h>
int main (void)
{
    int values[5];
    for (int i = 0; i < 5; i++){
        scanf("%d", &values[i]);
        printf("The num is%d\n", values[i]);
    } 
}