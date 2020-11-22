#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int i, score[11],max=1,min=0;
  float average=0.0,s=0.0;
  for(i=1;i<=10;i++){
  scanf("%d",&score[i]);
  //printf("%d\n",score[i]);
  }
      for(i=1;i<=10;i++){
      if (max<score[i])
      max= score[i];
      }    
  for(i=1;i<=10;i++){
      if(min>score[i])
      min= score[i];
      }
      for(i=1;i<=10;i++){
          s+=score[i];
          }
          average= (s-min-max)/8;
      printf("%f",average);
  system("PAUSE");	
  return 0;
}
