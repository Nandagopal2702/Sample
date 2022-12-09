// # include <stdio.h>
// int main(){
//     int num1;
//     int num2;
//     printf("enter 1st number:");
//     scanf("%d",&num1);
//     printf("enter 2nd number:");
//     scanf("%d",&num2);
//     printf("The sum of this number is:%d",num1+num2);
//     return 0;
// }

# include <stdio.h>
int main(){
    int x=0, y=0, result=0;
    printf("enter 1st number:");
    scanf("%d",& x);
    printf("enter 2nd number:");
    scanf("%d",& y);
    result = x+y;
    printf("The sum of this number is:%d",result);
    return 0;
}