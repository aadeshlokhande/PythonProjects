#include<stdio.h>
int main()
{
    int a=9;
    for (int i = 0; i < 10; i++)
    {
        printf("%d%d\n",i,a);
        a--;
    }
    return 0;
}