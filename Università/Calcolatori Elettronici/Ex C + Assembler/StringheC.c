#include <stdio.h>

void stampa_stringa(char *s){
	
	/* Il fatto che la funzione è impostata per avere in entrata un elemento del tipo *s,
	   può sembrare fuorviante. Questo tipo di dichiarazione implica semplicemente che il valore
	   passato alla funzione sia un indirizzo. Come vedremo sotto, nelle due dichiarazioni di stringhe,
	   s e t rappresentano due indirizzi quindi passo quelli alla funzione. 
	   
	   Da chiararire questo:
	   
	   !!!	ALLA FUNZIONE DEVO PASSARE UN INDIRIZZO, NON PER FORZA UN PUNTATORE !!! */
	   
int len;
for (len = 0; *s != '\0'; ++len){
     
     ++s;
}
}

int main(void){

char *s = "Stringa"; /* Primo modo di definire una stringa */
char t[] = "Stringa2"; /* Secondo modo per definire una stringa */

printf("\nCosa restituisce il valore s? %d Ed il valore t? %d", s, t);
printf("\nCosa restituisce il valore *s? %c Ed il valore *t? %c", *s, *t);
++s;
printf("\n\nCosa restituisce il valore s dopo averlo incrementato?%d", s);
printf("\nCosa restituisce ora *s? %c", *s);

stampa_stringa(s);

stampa_stringa(t);

return 0;

}
