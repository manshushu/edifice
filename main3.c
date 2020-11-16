#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int gz,ynsgz,shui;
    printf("请输入您的工资\n");
    scanf("%d",&gz);
    ynsgz=gz-3500;
    if
        (ynsgz<=1500)
        {shui=ynsgz*0.03;        
    }    
        if 
            (ynsgz>1500&&ynsgz<=4500)
        
        {shui=ynsgz*0.1-105;
        }        
        if
         (ynsgz<=9000&&ynsgz>4500)
       { shui=ynsgz*0.2-555;}        
       if
         (ynsgz<=35000&&ynsgz>9000)
       { shui=ynsgz*0.25-1005; }     
       
        printf("你应该缴纳个税%d\n",shui);
        
        
    system("PAUSE");	
  return 0;
}
