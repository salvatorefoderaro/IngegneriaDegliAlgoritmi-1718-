 
#include <stdio.h>

int main(void)
{
    char *s = "ciao"; // Modo per definire una stringa in C
    char p[]= "ciao"; // Altro modo per definire una stringa in C, Char[5]       

    printf("%c", *s); // Stampa c
    printf("%c", *p); // Stampa c

	p[0] = 'm'; // Posso farlo, essendo P nella sezione data e non in rodata
	
#Le differenze tra i due, sono tra i tipi di dato della variabile. Bisogna aggiungere che la prima delle due è una stringa "rodata", cioè possiamo solamente leggerla
#ed abbiamo che la stringa non è modificabile.
#La seconda dichiarazione, dichiara un array di caratteri il cui tipo è data, quindi è possibile accedervi e modificarla.
	
return 0;
}