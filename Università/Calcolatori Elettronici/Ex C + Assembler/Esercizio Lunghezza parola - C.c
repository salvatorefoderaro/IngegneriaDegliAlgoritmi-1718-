/*
 * Scrivere un programma C data in input una stringa e controlla che la lunghezza delle parole sia minore
 * di un valore L uguale a 3.
 */

#include <stdio.h>

/* Utilizzo questa sintassi in modo da definire L come una variabile di sola lettura e che quindi
   non può essere modificata. */

   #define L 3

void controllo_parola(char *s){

/*  Come al solito, visto che lavoro con caratteri, passo alla funzione un indirizzo.
	Il "void" è presente in quanto la funzione non restituisce nulla, ma stampa solamente un messaggio
	di errore o di correttezza della stringa inserita */


char *c; /* Utilizzo un puntatore di "supporto" */
int len;  /* Definisco un intero len che servirà per controllare la lunghezza della singola parola */

for (c = s; *c != '\0'; ++c){
	 /* 1) Assegno a c l'indirizzo base di s;
		2) Eseguo il ciclo for fin quando *c è diverso da '\0', cioè fin quando il carattere
		   che sto controllando non è il terminatore della stringa
		3) Incremento c, cioè l'indirizzo base della stringa, per accedere al carattere successivo */
	
	if(*c == ' '){
		/* Se il carattere che controllo è uno spazio, significa che la parola è terminata e dunque imposto
		   la lunghezza a 0. */
		len = 0;
		
	} else {
		/* Nel caso in cui non incontro uno spazio, incremento la lunghezza della parola. */
		++len;
	}

	if (len > L){
		/* Controllo che la lunghezza della parola sia minore del valore L definito (nel nostro caso è 3) */
		printf("Errore, non tutte le lunghezze sono state rispettate!");
		/* Se la lunghezza è maggiore del valore limite, allora tramite "break" esco dal ciclo */
		break;
	}
}

if (len <= L){
	
	/* Effettuo il controllo sull'ultima parola della stringa. */
	
	printf("Tutte le lunghezze sono state rispettate!");
}

};


int main(void){
	
	/* La funzione main è definita come int in quanto deve restituire un intero (return 0). 
	   Il Void implica che nessun argomento viene passato "dall'esterno", in quanto la definizione della stringa
	   avviene al suo interno.
	*/

char *s = "Parola da controllare"; /* Definisco la stringa di caratteri da controllare */

controllo_parola(s);


return 0;

}

