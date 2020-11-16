#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{int h,m,s,h1,m1,s1,jiange;
scanf("%d:%d:%d %d:%d:%d",&h,&m,&s,&h1,&m1,&s1);
jiange=s1+60*m1+3600*h1-s-60*m-3600*h;
      
    printf("时间间隔=%02d:%02d:%02d\n",jiange/3600,(jiange-jiange/3600*3600)/60,jiange-jiange/3600*3600-((jiange-jiange/3600*3600)/60*60));
    if (jiange<=7200)
    {printf("你能享受公交优惠1元\n");
    }
    else{
        printf("对不起，你不能享受公交优惠\n");}
  
  system("PAUSE");	
  return 0;
}
