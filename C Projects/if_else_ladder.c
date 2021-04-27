/*
if else ladder syntax:-

if(condition)
{
    statements;
}
else if(condition)
{
    statemets;
}
else if(condition)
{
    statement
}
else if(condition)
{
    statement
}
else if(condition)
{
    statement
}
else
{
    statements;
}

*/

#include<stdio.h>
int main()
{
    int date,temp;

    printf("Enter a number = ");
    scanf("%d",&temp);

    date = temp%7;
    if((temp<=31)&&(temp>0))
    {
        if(date==1)
        {
            printf("monday\n");
        }
        else if(date==2)
        {
            printf("tuesday\n");
        }
        else if (date==3)
        {
            printf("wednesday\n");
        }
        else if (date==4)
        {
            printf("thursday\n");
        }
        else if (date==5)
        {
            printf("friday\n");
        }
        else if (date==6)
        {
            printf("saturday\n");
        }
        else if (date==0)
        {
            printf("sunday\n");
        }
    }
    
    return 0;
}





/*


(a+b)>c
(a+c)>b
(c+b)>a






*/