#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int cunqi;
  float benjin,lixi;
  printf("������ı���ʹ���"); 
  scanf("%f %d",&benjin,&cunqi);
  switch(cunqi){
      case 1 :
          lixi=benjin*cunqi*0.035;
          printf("��Ϣ��%f",lixi);
          break;
          case 2 :
          lixi=benjin*cunqi*0.044;
          printf("��Ϣ��%f",lixi);
          break;
          case 3 :
          lixi=benjin*cunqi*0.05;
          printf("��Ϣ��%f",lixi);
          break;
          case 5 :
          lixi=benjin*cunqi*0.065;
          printf("��Ϣ��%f",lixi);
          break;
          default:  
      printf("����Ĵ�������\n");
      //return 1;
      }
      
   
  system("PAUSE");	
  return 0;
}
