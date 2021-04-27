/*
4 function and 1 main function
1 add
2 sub
3 multi
4 modulus


escape char:
\n = new line
\t =  tab 
\\ = backslace

*/

#include<stdio.h>

void add(int a, int b)
{
    printf("%d + %d = %d\n",a,b,a+b);
}

void sub(int a, int b)
{
    printf("%d - %d = %d\n",a,b,a-b);
}

void multi(int a, int b)
{
    printf("%d x %d = %d\n",a,b,a*b);
}
void mod(int a, int b)
{
    printf("%d %% %d = %d\n",a,b,a%b);
}

int main()
{
    int a,b;
    printf("Enter a number = ");
    scanf("%d",&a);
    printf("Enter a number = ");
    scanf("%d",&b);
    add(a,b);
    sub(a,b);
    multi(a,b);
    mod(a,b);
    return 0;
}
