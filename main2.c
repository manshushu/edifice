#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{int h,m,s,h1,m1,s1,jiange;
scanf("%d:%d:%d %d:%d:%d",&h,&m,&s,&h1,&m1,&s1);
jiange=s1+60*m1+3600*h1-s-60*m-3600*h;
      
    printf("ʱ����=%02d:%02d:%02d\n",jiange/3600,(jiange-jiange/3600*3600)/60,jiange-jiange/3600*3600-((jiange-jiange/3600*3600)/60*60));
    if (jiange<=7200)
    {printf("�������ܹ����Ż�1Ԫ\n");
    }
    else{
        printf("�Բ����㲻�����ܹ����Ż�\n");}
  
  system("PAUSE");	
  return 0;
}
