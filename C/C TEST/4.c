#include <stdio.h>
#include <string.h>
#include<assert.h>
#include <io.h>
int main()
{
    char filename[]="HELLO";
    char buf[100]="";
    int file;
    file=creat(filename,0);//创建文件
    assert(file!=-1);
    printf("input file content:,end with \"##\":\n");//输入文件内容，##表示结束
    while (1)
    {
        gets(buf);//输入一行
        strcat(buf, "\r\n");//加入换行符
        if (strcmp(buf, "##\r\n")==0)//遇到##退出
            break;

        _write(file, buf, strlen(buf));
    }
    _close(file);//关闭文件
    return 0;
}