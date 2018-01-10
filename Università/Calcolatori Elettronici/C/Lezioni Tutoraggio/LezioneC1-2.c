#include <stdio.h>

int main(void)
{
	char a; // 8 bit
	int b;  // 16 o 32 bit
	short int c; // 16 bit
	long int d; // 32 o 64 bit
	long long int e; // >= 64 bit
		
	float f; // 32 bit
	double g; // 64 bit
	
	long double h; // 80 ai 128 bit
	
	// dim(char) <= dim(short) <= dim(lo	unsigned char i; // [0,2^8-1] => [0,255] - Senza segno
	signed char x; // [-2^7, +2^7-1] => [-128, +127] - Con il segno
	
	// -1 (8 bit)
	// valore assoluto 00000001 
	// negato: 11111110
	// somma1: 11111111
	
	// 255 (8 bit) = 11111111
	
	int array[7]:
	char s[] = "hello"; // Array di caratteri che viene "vista" come una stringa. Collezione oggetti dello stesso tipo, in questo caso int
    
    // s[0] .. s[5]
    // s[5] == 0	
	
	// array[0] ... array[n-1]
	
	return 0
}