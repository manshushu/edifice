#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int year,month,days;
    printf("请输入年份和月份\n");
    scanf("%d %d",&year,&month);
    switch(month){
        case 1 :
            printf("该月天数是31天");
        break;
        case 3 :
            printf("该月天数是31天");
        break;
        case 5 :
            printf("该月天数是31天");
        break;
        case 7 :
            printf("该月天数是31天");
        break;
        case 8 :
            printf("该月天数是31天");
        break;
        case 10 :
            printf("该月天数是31天");
        break;
        case 12 :
            printf("该月天数是31天");
        break;
        case 4 :
            printf("该月天数是30天");
        break;
        case 6 :
            printf("该月天数是30天");
        break;
        case 9 :
            printf("该月天数是30天");
        break;
        case 11 :
            printf("该月天数是30天");
        break;
        case 2 :
            if(year%4 == 0)
    {
        if( year%100 == 0)
        {
            
            if ( year%400 == 0)
                printf("该月天数是29天");
            else
                printf("该月天数是28天");
        }
        else
            printf("该月天数是29天");
    }
    else
        printf("该月天数是28天");
        } 
    
  
  system("PAUSE");	
  return 0;
}
