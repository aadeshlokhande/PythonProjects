#include <stdio.h>
void main()
{
    int option,roll_number,subject,
        marks[20][6] =     {{44,55,65,45,23,87},{32,42,52,54,87,34},
        {34,54,75,34,87,43},{43,63,78,53,23,65},{55,85,23,75,75,23},
        {22,52,54,47,33,23},{23,86,45,79,34,33},{42,23,85,33,52,65},
        {55,32,56,53,40,43},{53,73,86,53,23,54},{32,43,63,87,54,23},
        {23,86,45,79,34,33},{55,85,23,75,75,23},{32,43,63,87,54,23},
        {34,54,75,34,87,43},{32,42,52,54,87,34},{44,55,65,45,23,87},
        {53,73,86,53,23,54},{32,42,52,54,87,34},{44,55,65,45,23,87}};
    char exit;
    
    do{
        printf("\t\t\tResults\n\nPress 1 for Marks\nPress 2 for Result\nPress 3 for whole table\nEnter your choice = ");
        scanf("%d",&option);
        
        if(option>0 && option<4)
        {
            switch(option)
            {
                case (1):
                printf("Enter a Roll Number = ");
                scanf("%d",&roll_number);
                if((roll_number<20)&&(roll_number>=0))
                {
                    printf("press\n1. = Marathi\n2. = Hindi\n3. = English\n4. = Maths\n5. = history\n6. = Geography\n");
                    printf("Enter your Choice = ");
                    scanf("%d",&subject);
                    if((subject<7)&&(subject>0))
                    {
                        subject--;
                        if(subject==0)
                        {
                            printf("Marks of Marathi = %d",marks[roll_number][subject]);
                        }
                        else if(subject==1)
                        {
                            printf("Marks of Hindi = %d",marks[roll_number][subject]);
                        }
                        else if(subject==2)
                        {
                            printf("Marks of English = %d",marks[roll_number][subject]);
                        }
                        else if(subject==3)
                        {
                            printf("Marks of Maths = %d",marks[roll_number][subject]);
                        }
                        else if(subject==4)
                        {
                            printf("Marks of History = %d",marks[roll_number][subject]);
                        }
                        else
                        {
                            printf("Marks of Geography = %d",marks[roll_number][subject]);
                        }
                    }
                    else
                    {
                        printf("\nInvalid subject");
                    }
                }
                else
                {
                    printf("\nInvalid Roll Number");
                }
                break;
            
                case (2):
                printf("Enter a Roll Number = ");
                scanf("%d",&roll_number);

                if((roll_number<20)&&(roll_number>=0))
                {
                    printf("\tResult Of Roll No. %d\n",roll_number);
                    printf("\nMarks of Marathi\t=\t %d\n",marks[roll_number][0]);
                    printf("\nMarks of Hindi\t\t=\t %d\n",marks[roll_number][1]);
                    printf("\nMarks of English\t=\t %d\n",marks[roll_number][2]);
                    printf("\nMarks of Maths\t\t=\t %d\n",marks[roll_number][3]);
                    printf("\nMarks of History\t=\t %d\n",marks[roll_number][4]);
                    printf("\nMarks of Geography\t=\t %d\n",marks[roll_number][5]);
                }
                else
                {
                    printf("Invalid Input");
                }
                break;
            
                case (3):
                printf("\n\n\t\tMar\tHin\tEng\tMath\tHis\tGeo\n\n");
                for (int i = 0; i < 20; i++) 
                {
                    printf("Roll No.%d =\t",i);
                    for (int j = 0; j < 6; j++) 
                    {
                        printf("%d\t", marks[i][j]);
                    }
                    printf("\n\n");
                }
                break;
                
                default:
                printf("Invalid Input");
            } 

            
        }
        else
        {
            printf("Wrong Input");
        }
        printf("\n\nDo you want to Continue Y/N = ");
        scanf(" %c", &exit); 
    }while (exit=='Y' || exit=='y');
    printf("Exit...!!!\n");
}