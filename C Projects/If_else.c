/*
if(conditions)
{
    statements;
    statements;
    statements;
    statements;
    statements;
}
else
{
    statements;
    statements;
    statements;
    statements;
}
*/


#include<stdio.h>
int main()
{
    int age;
    
    printf("Enter your age = ");
    scanf("%d",&age);

    if(age>18)
    {
        printf("tu gadi chalwu shakte...\n");
    }
    else
    {
        printf("tu gadi chalwu shakt nhi....\n");
    }
    return 0;
}