#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>

int main(int argc, char *argv[])
{
   int i, c, v = 0;
   if (argc < 2){
   printf("sintassi: %s <testo>\n", argv[0]);
   return 1;
   }
   
   for (i=0; argv[1][i] != '\0'; i++){
	   if (argv[1][i] == 'a' ||
           argv[1][i] == 'e' ||
		   argv[1][i] == 'i' ||
		   argv[1][i] == 'o' ||
		   argv[1][i] == 'u')
		   {
			   v++;
		   }

		   }
   c = i-v;	   
   printf("vocali: %d\n", v);
   printf("consonanti: %d\n", c);
   return 0;
}
