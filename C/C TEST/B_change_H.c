#include<stdio.h>
#include<assert.h>
char data[]="1011011010011110110101110";
int main()
{
    assert(data[0]!='\0');
    int sum=0;
    for(int i=0;i<sizeof(data)/sizeof(char)-1;i++)
    {
        assert(data[i]=='1'||data[i]=='0');
        sum<<=1;
        sum+=data[i]-'0';
    }
    printf("%x",sum);
    return 0;
}