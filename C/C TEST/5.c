/*************************************************************************
    > File Name: copy1.c
    > Author: jukay
    > Mail: hellojukay@163.com
    > Created Time: 2014年12月19日 星期五 20时51分11秒
 ************************************************************************/

#include<stdlib.h>
#include<stdio.h>
int main()
{
	FILE *fp,*out;
	unsigned char buffer[100];
	size_t n;
	fp = fopen("a.out","rb");
	out = fopen("backup","wb+");
	if(fp == NULL || out == NULL)
	{
		fprintf(stderr,"无法打开文件\n");
		exit(EXIT_FAILURE);
	}
	while((n = fread(buffer,sizeof(unsigned char),100,fp)) != 0)
	{
		fwrite(buffer,sizeof(unsigned char),n,out);
	}

	fclose(out);
	fclose(fp);
	exit(EXIT_FAILURE);
}

/*在上网的传播的病毒,大多都右自我复制能力,那他们是怎么复制自己的呢?
 * 今天就写了个小程序来实验下,这里默认程序自己的名字是a.out.程序是二进制文件,所以复制是
 * 对二进制文件的读写,而对文本文件的读写这里就不适合.(a.out可以mian函数的第一个参数来代替)<span style="font-family: Arial, Helvetica, sans-serif;"> */