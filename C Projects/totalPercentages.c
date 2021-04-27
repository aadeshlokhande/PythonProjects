#include<stdio.h>
int main()
{
    float marathi, hindi, english,history, geography, maths, totalmarks, percent;
    printf("Marks of Marathi = ");
    scanf("%f",&marathi);
    printf("Marks of Hindi = ");
    scanf("%f",&hindi);
    printf("Marks of English = ");
    scanf("%f",&english);
    printf("Marks of History = ");
    scanf("%f",&history);
    printf("Marks of Geography = ");
    scanf("%f",&geography);
    printf("Marks of Maths = ");
    scanf("%f",&maths);
    totalmarks = marathi+hindi+english+history+geography+maths;
    percent = (totalmarks/600)*100;
    printf("percent = %f \n",percent);
    if (34 >= percent)
    {
        printf("You Are Fail");
    }
    else if (50 > percent)
    {
        printf("you are pass with C grade");
    }
    else if (75 > percent)
    {
        printf("you are pass with B grade");
    }
    else
    {
        printf("you are pass with A grade");
    }
    return 0;
}