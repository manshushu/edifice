#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int cunqi;
  float benjin,lixi;
  printf("输入存款的本金和存期"); 
  scanf("%f %d",&benjin,&cunqi);
  switch(cunqi){
      case 1 :
          lixi=benjin*cunqi*0.035;
          printf("利息是%f",lixi);
          break;
          case 2 :
          lixi=benjin*cunqi*0.044;
          printf("利息是%f",lixi);
          break;
          case 3 :
          lixi=benjin*cunqi*0.05;
          printf("利息是%f",lixi);
          break;
          case 5 :
          lixi=benjin*cunqi*0.065;
          printf("利息是%f",lixi);
          break;
          default:  
      printf("输入的存期有误\n");
      //return 1;
      }
      
   
  system("PAUSE");	
  return 0;
}
