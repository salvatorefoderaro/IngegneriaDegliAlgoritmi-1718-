#include <stdio.h>


void funzione(int a){
	
	a = 1000;
	printf("\nIl valore di a dentro la funzione è %d", a);
	
}

void funzione_puntatore(int *a){
	
	*a = 1000;
	printf("\nIl valore di a dentro la funzione è %d", *a);
	
}


int main(void){
	
	int a = 10;
	
	funzione(a);
	printf("\nIl valore di a dopo funzione(a) è %d", a);
	funzione_puntatore(&a);
	printf("\nIl valore di a dopo funzione_puntatore(a) è %d", a);

	int b = 100; /* Assegno alla variabile b il valore 100 */
	printf("\n\nIl valore iniziale di b è %d", b);
	int *c; /* Creo un puntatore c */	
	c = &b; /* Assegno al puntatore c l'indirizzo di b */
	*c = 10000; /*Assegno all'elemento puntato da c il valore 10000 */

	
	printf("\nCosa mi restituisce l'elemento c? %d", c);
	printf("\nQual'è l'indirizzo di b? %d", &b);
	printf("\nQual'è il valore di b? %d E quello di *c? %d", b, *c);
	
	return 0;
}