#include<stdio.h>
int main()
{
   int a,b;
   
   printf("A = ");
   scanf("%d",&a);

   printf("B = ");
   scanf("%d",&b);
   
   printf("%d + %d = %d \n",a,b,a+b);
   printf("%d - %d = %d \n",a,b,a-b);
   printf("%d * %d = %d \n",a,b,a*b);
   printf("%d / %d = %d \n",a,b,a/b);
   printf("%d mod %d = %d \n",a,b,a%b);

   return 0;
}