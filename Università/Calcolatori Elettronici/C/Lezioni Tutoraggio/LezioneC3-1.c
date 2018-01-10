#include <stdio.h>

// Blocco di codice, incluso tra due parentesi graffe

 int main(void)
 {
	 int a=5;
	 
	 {
		 a += 1; // La variabile iniziale a aumenta di 1, in quanto mi riferisco ancora a lei
		 int a = 10; // Avendo dichiarato una nuova variabile, ora all'interno del blocco
		             // Lavoro solamente con questa a, quindi il fatto che abbia tutte e due stesso nome fa niente
		 a += 2;
		 printf("a=%d\n", a);
	 }
	 printf("a=%d\n", a);
	 return 0;
	 
	 return 0;
 }
 
 int a = 6; // Corrisponde al Global di Python
 
 int manin(void)
 {
	 return 0;
 }
 
 // Funzioni
 
 int f(int a, int b) // a e b variabili automatiche, valgono solamente all'interno della funzione
 {
	 ...
 }