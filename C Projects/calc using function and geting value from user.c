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
    int a,b,c;
    printf("Enter 1st value = ");
    scanf("%d",&a);
    printf("Enter 2nd value = ");
    scanf("%d",&b);
    printf("add = 1\nsub = 2\nmulti = 3\nmod = 4\nEnter a number = ");
    scanf("%d",&c);
    switch(c)
    {
        case 1:
        add(a,b);
        break;
        
        case 2:
        sub(a,b);
        break;
        
        case 3:
        multi(a,b);
        break;
        
        case 4:
        mod(a,b);
        break;
        
        default:
        printf("invalid input");
        break;
    }
    
    return 0;
}













