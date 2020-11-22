#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int x;
  for(x=7;x<=1e5;x+=7){
      if(x%2==1 && x%3==2 && x%5==4 && x%6==5)
     break;
       
      } 
       printf("Â¥ÌÝÖÁÉÙÓÐ%d½×\n",x);
  system("PAUSE");	
  return 0;
}
