#include<stdio.h>
#include<malloc.h>
#include<assert.h>
int main()
{
    char *DATA=(char*)malloc();
    int Ori=0,Res=0;
PART:
    
    fflush(stdin);
    if(Ori==0)
    {
        printf("Input the Ori\n");
        scanf("%d",&Ori);
        fflush(stdin);
    }
    if(Res==0)
    {
        printf("Input the Res\n");
        scanf("%d",&Res);
        fflush(stdin);
    }

    while()
    {

    }

    fflush(stdin);
    if(getchar()!='N')
    {
        goto PART;
    }
    return 0;
}