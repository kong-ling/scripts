// AES.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int main()
{
	char c;
	char a_char[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
	unsigned int a_int[] = { 0x33221100, 0x77665544, 0xbbaa9988, 0xffeeddcc, 0x55667788, 0x66778899, 0x778899aa, 0x8899aabb };
	unsigned int keys[][4] =
	{
		/*0, test set 1*/{ 0xd3c5d592, 0x327fb11c, 0x4035c668, 0x0af8c6d1 },
		/*1, test set 2*/{ 0x2bd6459f, 0x82c440e0, 0x952c4910, 0x4805ff48 },
		/*2, test set 3*/{ 0x0a8b6bd8, 0xd9b08b08, 0xd64e32d1, 0x817777fb },
		/*3, test set 4*/{ 0xaa1f95ae, 0xa533bcb3, 0x2eb63bf5, 0x2d8f831a },
		/*4, test set 5*/{ 0x9618ae46, 0x891f8657, 0x8eebe90e, 0xf7a1202e },
		/*5, test set 6*/{ 0x54f4e2e0, 0x4c83786e, 0xec8fb5ab, 0xe8e36566 }
	};

	printf("%d", sizeof(a_char));
	printf("%d", sizeof(a_int));

	for (int i = 0; i < sizeof(a_char); i++)
	{
		printf("a_char[%d]=%d\n", i, a_char[i]);
	}
	

	for (int i = 0; i < sizeof(a_int)/sizeof(int); i++)
	{
		printf("a_int[%02d]=%08X\n", i, a_int[i]);
	}

	for (int i = 0; i < sizeof(a_int); i++)
	{
		printf("a_byte[%02d]=0x%02X, addr=0x%08X\n", i, *(((unsigned char *)a_int) +i), ((unsigned char *)a_int) + i);
	}

	for (int i = 0; i < sizeof(keys)/sizeof(keys[0]); i++)
	{
		printf("%d: 0x%08X, 0x%08X\n", i, keys[i][0], &keys[i]);
	}

	printf("double=%d\n", sizeof(double));
	printf("long long=%d\n", sizeof(long long));


	printf("Press any key to continue\n");
	scanf_s("%c", &c);
	return 0;
}

