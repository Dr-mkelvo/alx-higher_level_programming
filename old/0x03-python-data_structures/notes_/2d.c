#include <stdio.h>
const int CITY = 2;
const int WEEK = 7;
int main(void)
{
    int temp[CITY][WEEK];
    for (int i = 0; i < CITY; i++)
    {
        for(int j = 0; j < WEEK; j++)
        {
        printf("City %d Day %d :", i + 1, j + 1);
        scanf("%d", &temp[i][j]);
        printf("Results %d", temp[i][j]);
        }
    }

}