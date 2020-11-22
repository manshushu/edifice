#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{     long i=1,a=1;
      double n=1.0,s=0;

for(a=1;a<=n;a++)
{     
          for(i=1;i<=1e30;i++){
              n*=i;
              s+=1.0/n;
              if ((1.0/n)<1e-6)
          
          break;
              }
}
printf("%lf\n",s);
  system("PAUSE");	
  return 0;
}
