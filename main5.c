#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int year,month,days;
    printf("��������ݺ��·�\n");
    scanf("%d %d",&year,&month);
    switch(month){
        case 1 :
            printf("����������31��");
        break;
        case 3 :
            printf("����������31��");
        break;
        case 5 :
            printf("����������31��");
        break;
        case 7 :
            printf("����������31��");
        break;
        case 8 :
            printf("����������31��");
        break;
        case 10 :
            printf("����������31��");
        break;
        case 12 :
            printf("����������31��");
        break;
        case 4 :
            printf("����������30��");
        break;
        case 6 :
            printf("����������30��");
        break;
        case 9 :
            printf("����������30��");
        break;
        case 11 :
            printf("����������30��");
        break;
        case 2 :
            if(year%4 == 0)
    {
        if( year%100 == 0)
        {
            
            if ( year%400 == 0)
                printf("����������29��");
            else
                printf("����������28��");
        }
        else
            printf("����������29��");
    }
    else
        printf("����������28��");
        } 
    
  
  system("PAUSE");	
  return 0;
}
