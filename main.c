#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{ 
       int a1 = 0,b1 = 0,c1 = 0;
    char a;

    while ( ( a=getchar() ) != '\n')
    {
    
        if(a >= '0'&&a<='9')
        {
            a1++;
        }
        else if(a >= 'a' &&  a <= 'z')
        {
            b1++;
        }
        else if(a >= 'A' && a <= 'Z')
        {
            b1++;
        
        }
        else
        {
            c1++;
        }

    }
    printf("数字字符为%d个,英文字母为%d个,其他字符为%d个\n",a1,b1,c1); 

    
  system("PAUSE");	
  return 0;
}
