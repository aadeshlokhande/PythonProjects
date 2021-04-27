#include<stdio.h>
int main()
{
	float x, y;

	printf("\n\t\t\tEnter Co-ordinates point");
	
	printf("\n\n\tEnter X co-ordinate  = ");
	scanf(" %f", &x);
	
	printf("\n\tEnter Y co-ordinate  = ");
    scanf(" %f", &y);
	
	if((x>0)&&(y>0))
    {
		printf("\n  The point lies in First quadrant ");	
	}
	else if((x<0)&&(y>0))
	{
		printf("\n  The point lies in Second quadrant ");	
	}
	else if((x<0)&&(y<0))
	{
		printf("\n  The point lies in Third quadrant ");
	}
	else if ((x>0)&&(y<0))
	{
		printf("\n  The point lies in Fourth quadrant ");	
	}
	else if((x==0)&&(y==0))
	{
		printf("\n  The point lies in origin");
	} 
	else if((x==0)&&(y>0))
	{
		printf("\n  The point lies on Y-axis");
	}
	else if((x==0)&&(y<0))
	{
		printf("\n  The point lies on Y-axis");	
	}
	else if((x>0)&&(y==0))
	{
		printf("\n  The point lies on X-axis");
	}
	else if((x<0)&&(y==0))
	{
		printf("\n  The point lies on X-axis");
	}
	else 
	{
		printf("\n  Invalid Input");
	}	
	return 0;
}