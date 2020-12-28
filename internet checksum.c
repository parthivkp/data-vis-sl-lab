#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int checksum(int fl){
    int n,i,temp=0,sum=0;
    char in[200];
    scanf("%s",&in);
    if(strlen(in)%2!=0)
    n=(strlen(in)+1)/2;
    else
    {
        n=(strlen(in)/2);
    }for(i=0;i<n;i++){
        temp=in[i*2];
        temp=(temp*256)+in[(i*2)+1];
        sum=sum+temp;
    }if(fl==1){
        printf("Enter checksum\n");
        scanf("%x",&temp);
        sum=sum+temp;
    }if(sum%65536!=0){
        n=sum%65536;
        sum=(sum/65536)+n;
    } sum=65535-sum;
    return sum;
    
}
void main(){
    int ch=1,sum;
    while(ch){
    printf("\n1.ENCODE\n2.DECODE\n0.EXIT\n");
    scanf("%d",&ch);
    switch (ch){
        case 1 :printf("Enter string\n");
                sum=checksum(0);
                printf("Checksum to append is %x",sum);
                break;
        case 2: printf("Enter string\n");
                sum=checksum(1);
                if(sum!=0){
                    printf("Invalid checksum ERROR!!!\n");
                    break;
                }else {
                    printf("Valid Data\n");
                }
    }
}
}