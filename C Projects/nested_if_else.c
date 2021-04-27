#include<stdio.h>
int main()
{
    int age,marks;
    
    printf("Enter your age = ");
    scanf("%d",&age);
    
    if(age>=20)
    {
        printf("Enter your marks = ");
        scanf("%d",&marks);
        if(marks>=70)
        {
            printf("Welcome to clg");
        }
        else
        {
            printf("marks kami ahe");
        }
    }
    else
    {
        printf("you are under age");
    }
    
    
    

    return 0;
}