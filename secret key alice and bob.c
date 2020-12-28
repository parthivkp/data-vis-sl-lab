#include<stdio.h>
#include<stdlib.h>

int compute(int a,int m,int n){
    int y=1;
    int r;
    while(m>0){
        r=m%2;
        if(r==1)
        y=(y*a)%n;
        a=(a*a)%n;
        m=m/2;
    } return y;
}


int main(){
    int p=23,g=5;
    int a,b,A,B;
    a=6,b=15;
    A=compute(g,a,p);
    B=compute(g,b,p);
    int keya=compute(B,a,p);
    int keyb=compute(A,b,p);
    printf("Alice secret key is %d\nbob's secret key is %d",keya,keyb);
}