#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int x,y,z;
  for(x=1;x<20;x++){
      for(y=1;y<33;y++){
          for(z=3;z<90;z+=3){
              if (5*x+3*y+z/3==100 && x+y+z==100)
              printf("公鸡为%d 母鸡为%d 小鸡为%d\n",x,y,z);
              }
          }
      }
      //printf("公鸡为%d 母鸡为%d 小鸡为%d\n",x,y,z);
  system("PAUSE");	
  return 0;
}
