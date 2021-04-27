/*
for loop syntax:-
for(int;cond;inc/dec)
{
    state'
}
*/


// #include<stdio.h>
// int main()
// {
//     int sum=0;
//     for(int a=1 ; a<11 ; a++)
//     {
//         sum = sum + a;
//         printf("%d ",a);
//     }

//     printf("sum = %d",sum);
//     return 0;
// }




// #include<stdio.h>
// int main()
// {
//     int a,b;

//     printf("Enter start = ");
//     scanf("%d",&a);
    
//     printf("Enter End = ");
//     scanf("%d",&b);

//     for(int i = a;i<=b; i++)
//     {
//         if(i%2==0)
//         {
//             printf("%d, ",i);
//         }
//     }
    
//     return 0;
// }


// #include<stdio.h>
// int main()
// {
//     int a,i;
//     printf("Enter number = ");
//     scanf("%d",&a);

//     for(i=1; i<=a;i++)
//     {
//         printf("%d\n",i*i*i);
//     }

//     return 0;
// }



// #include<stdio.h>
// int main()
// {
//     int a,b=0,c;
//     printf("Enter number = ");
//     scanf("%d",&a);
//     for(c =1; c<=a;c++)
//     {
//         if(a%2!=0)
//         {
//             printf("%d ",c);
//             b = b + c;
//         }
//     }
//     printf("sum = %d",b);

//     return 0;
// }




// // prime number
// #include<stdio.h>
// int main()
// {
//     int num,i,count = 0;
//     printf("enter a number = ");
//     scanf("%d",&num);               // 18
//     for(i=2; i<=num/2; i++)         // 9
//     {
//         if(num%i==0)
//         {
//             count++;            
//             break;
//         }
//     }
//     if((count==0) && (count!=1))
//     {
//         printf("%d is prime number",num);
//     }
//     else
//     {
//         printf("%d is not prime number");
//     }
//     return 0;
// }




#include<stdio.h>
int main()
{
    
    int a = 65;

    for(int i= 1;i <= 13;i++)
    {
        for(int j = 1; j < 3; j++)
        {
            printf("%c ",a);
            a++;
        }
    }
    return 0;
}
