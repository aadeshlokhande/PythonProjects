/*
switch case syntax:

switch(argument)
{
    case(1):
    statements;
    break;

    case(2):
    statements
    break;
    .
    .
    .
    .
    .

    case (n):
    statements;
    break;

    default:
    statemnts;
    break;
}
*/



// #include<stdio.h>
// int main()
// {
//     char op;

//     printf("Enter a number = ");
//     scanf(" %c", &op);

//     switch(op)
//     {
//         case ('+'):
//         printf("january\n");
//         break;

//         case ('-'):
//         printf("feb\n");
//         break;

//         default:
//         printf("invalid input");
//         break;
//     }
//     return 0;
// }

/*
swtch case
balance = 5000
pin 1234
enter 1 for withdraw
    enter a pin = 1234
        enter a amount = 500
        withdraw successful 
        balance = 4500 
    or
        wrong pin

2 for balance check
    enter a pin  = 1234
        balance = 5000
    or 
         wrong pin
3 for pin change 
    enter a old pin
        enter new pin = 0099
            confirm your pin = 0099
                pin changed
            or 
                try again
    or 
        wrong pin

4 for close
    closed
*/



// #include<stdio.h>
// int main()

// {
// 	int num , a, b;
	
// 	printf("\n\nEnter a number = ");
// 	scanf(" %d", &num);
	
// 	a= num/10;
// 	b= num%10;
	
// 	if((num>99)||(num<0))
// 	{
// 		printf("\n\nEnter a number between 20-99");
// 	}
// 	else 
// 	{
		
// 	switch(a)
// 	{
//      case (2) :
//      printf(" %d = Twenty", num);
//      break;
//      case (3) :
//      printf(" %d = Thirty", num);
//      break;
// 	 case (4) :
//      printf(" %d = Fourty", num);
//      break;
// 	 case (5) :
//      printf(" %d = Fifty", num);
//      break;
// 	 case (6) :
//      printf(" %d = Sixty", num);
//      break;
// 	 case (7) :
//      printf(" %d = Seventy", num);
//      break;
// 	 case (8) :
//      printf(" %d = Eighty", num);
//      break;
// 	 case (9) :
//      printf(" %d = Ninety", num);
// 	 break;
// 	 } 
	
// 	switch(b)
// 	{
//      case (1) :
//      printf("-One");
//      break;
//      case (2) :
//      printf("-Two");
//      break;
//      case (3) :
//      printf("-Three");
//      break;
//      case (4) :
//      printf("-Four");
//      break;
//      case (5) :
//      printf("-Five");
//      break;
//      case (6) :
//      printf("-Six");
//      break;
//      case (7) :
//      printf("-Seven");
//      break;
//      case (8) :
//      printf("-Eight");
//      break;
//      case (9) :
//      printf("-Nine");
//      break;
// 	 } 
	
//     }
    
// 	return 0;
// }



// // vivek program number to words
// #include<stdio.h>
// int main()

// {
// 	int num , a, b, c, x;
	
// 	printf("\n\nEnter a number = ");
// 	scanf(" %d", &num);
	
// 	a= num/100;
// 	x= num/10;
// 	b= x%10;
// 	c= num%10;
	
// 	 if((num>1000)||(num<0))
// 	{
// 		printf("\n\nEnter a number between 0-1000");
// 	}
	
// else
// {

//   {	
// 	switch(a)
// 	{
// 	  case(1) :
// 	  printf(" %d = One Hundred", num);
// 	  break;
// 	  case(2) :
// 	  printf(" %d = Two Hundred", num);
// 	  break;
// 	  case(3) :
// 	  printf(" %d = Three Hundred", num);
// 	  break;
// 	  case(4) :
// 	  printf(" %d = Four Hundred", num);
// 	  break;
// 	  case(5) :
// 	  printf(" %d = Five Hundred", num);
// 	  break;
// 	  case(6) :
// 	  printf(" %d = Six Hundred", num);
// 	  break;
// 	  case(7) :
// 	  printf(" %d = Seven Hundred", num);
// 	  break;
// 	  case(8) :
// 	  printf(" %d = Eight Hundred", num);
// 	  break;
// 	  case(9) :
// 	  printf(" %d = Nine Hundred", num);
// 	  break; 	
// 	}
		
// 	switch(b)
// 	{
//      case (2) :
//      printf(" Twenty");
//      break;
//      case (3) :
//      printf(" Thirty");
//      break;
// 	 case (4) :
//      printf(" Fourty");
//      break;
// 	 case (5) :
//      printf(" Fifty");
//      break;
// 	 case (6) :
//      printf(" Sixty");
//      break;
// 	 case (7) :
//      printf(" Seventy");
//      break;
// 	 case (8) :
//      printf(" Eighty");
//      break;
// 	 case (9) :
//      printf(" Ninety");
// 	 break;
// 	 } 
	
// 	switch(c)
// 	{
//      case (1) :
//      printf("-One");
//      break;
//      case (2) :
//      printf("-Two");
//      break;
//      case (3) :
//      printf("-Three");
//      break;
//      case (4) :
//      printf("-Four");
//      break;
//      case (5) :
//      printf("-Five");
//      break;
//      case (6) :
//      printf("-Six");
//      break;
//      case (7) :
//      printf("-Seven");
//      break;
//      case (8) :
//      printf("-Eight");
//      break;
//      case (9) :
//      printf("-Nine");
//      break;
// 	 } 
	
//     }
// }
  
	
	
	
// 		if(num==0)
// 		{
// 		printf(" %d = Zero", num);
// 		}
		
// 		if(num==10)
// 		{
// 		printf(" %d = Ten", num);	
// 		}
// 		if(num==11)
// 		{
// 		printf(" %d = Eleven", num);	
// 		}
// 		if(num==12)
// 		{
// 		printf(" %d = Twelve", num);	
// 		}
// 		if(num==13)
// 		{
// 		printf(" %d = Thirteen", num);	
// 		}
// 		if(num==14)
// 		{
// 		printf(" %d = Fourteen", num);
// 		}
// 		if(num==15)
// 		{
// 		printf(" %d = Fifteen", num);
// 		}
// 		if(num==16)
// 		{
// 		printf(" %d = Sixteen", num);
// 		}
// 		if(num==17)
// 		{
// 		printf(" %d = Seventeen", num);
// 		}
// 		if(num==18)
// 		{
// 		printf(" %d = Eighteen", num);
// 		}
// 		if(num==19)
// 		{
// 		printf(" %d = Nineteen", num);
// 		}

// 		else if(num==1000)
// 		{
// 		printf(" %d = One Thousand", num);	
// 		}
//    return 0;
// }