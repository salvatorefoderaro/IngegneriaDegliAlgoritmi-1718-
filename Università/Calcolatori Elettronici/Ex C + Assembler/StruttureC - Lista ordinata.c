/*
 * Scrivere un programma C che richieda all'utente di digitare dei numeri interi
 * in input e li memorizzi in una lista collegata. 
 * La fase di input termina quando l'utente inserisce un numero
 * negativo; a quel punto, il programma stampa il contenuto della lista e termina.
 */
 
#include <stdlib.h>
#include <stdio.h>

/* Come al solito creo una struttura nodo come già visto */ 

struct nodo {
	int valore;
	struct nodo *successivo;
};

/*  Posso ed anzi devo mantenere una struttura di appoggio, in questo caso per mantenere il primo numero della lista ordinata.
	Il primo elemento sarà un nodo, dunque avrà tutte le proprietà dei nodi "classici" */
	
struct lista_interi {
	struct nodo *primo;
	int numero_elementi;
};

void inserisci_in_lista (struct lista_interi *lista, int valore)
{
	
	/* Per prima cosa creo un puntatore del tipo nodo, a cui associo il valore passato alla funzione */
	struct nodo *nuovo_nodo;
	nuovo_nodo->valore = valore;

	if (lista->primo == NULL || lista->primo->valore > valore) {
		/* Se il primo elemento della lista è NULL, cioè la lista è vuota, oppure il valore dell'elemento che vogliamoLa
		   inserire è maggiore del valore del primo elemento in lista, allora inserisco il nuovo nodo come primo.*/
		   
		nuovo_nodo->successivo = lista->primo;
		lista->primo = nuovo_nodo;
	} else {
		
		/* Inserisco il nodo in un'altra posizione della lista, ricordando però che deve essere sempre in una posizione
		   ordinata rispetto agli elementi già presenti.
		   
		   1) Utilizzo un puntatore di appoggio n, a cui associo l'indirizzo del primo elemento della lista.
			  E' giusto un modo per semplificare la sintassi di tutto il programma.
		   2) Fin quando l'indirizzo del nodo successivo è diverso da NULL ed il valore del nodo successivo
			  è minore del valore del nodo che voglio inserire, procedo con il controllo del nodo successivo.
			  
			  Cioè faccio questo per capire dove è che devo inserire questo nodo in pratica. Quindi visto che io so che
			  il nodo che voglio inserire è maggiore del nodo n, cioè del nodo lista->primo, non devo fare altro che controllare
			  il valore dell'elemento successivo. Se il valore dell'elemento successivo è maggiore, allora significa che il nuovo
			  nodo va inserito tra n ed il nodo n->successivo, dove n rappresenta il nodo al quale accedo tramite il ciclo for. */
		struct nodo *n;
		n = lista->primo;
		while (n->successivo != NULL && n->successivo->valore < valore)
			n = n->successivo;
		
		/* Quando esco dal ciclo For, e dunque ho che il nodo va inserito dopo n, procedo come già visto */
		nuovo_nodo->successivo = n->successivo;
		n->successivo = nuovo_nodo;
	}

}


void stampa_lista (struct lista_interi *l)
{
	/* Anche in questo caso utilizzo un puntatore ad una struttura di appoggio. */
	struct nodo *n;
	
	printf("La lista contiene %d elementi:\n", l->numero_elementi);
	
	/* Associo ad n il valore di l->primo, che ricordo è un indirizzo. Dunque è corretto, in quanto la variabile 
	   n indica un indirizzo, e l->primo contiene un indirizzo. Il resto è come abbiamo già visto. */
	for (n=l->primo; n!=NULL; n=n->successivo) {
		printf("%d\n", n->valore);
	}
}


int main()
{
	int valore_inserito;

	/* Definisco una lista vuota */
	struct lista_interi lista;
	lista.primo = NULL;  
	lista.numero_elementi = 0;

	printf("Inserisci dei numeri interi (inserire un valore negativo per terminare):\n");
	
	/* Questo è semplicemente il codice che permette l'inserimento di input da linea di comando.
	   Ad ogni inserimento, il valore viene salvato in valore_inserito e viene effettuta una chiamata
	   alla funzione per l'inserimento di quel valore in lista. Quando valore_inserito sarà uguale ad un numero negativo,
	   si esce dal ciclo.*/
	while (1) {
		int valori_letti = scanf("%d", &valore_inserito);
		if (valori_letti != 1 || valore_inserito < 0)
			break;

		inserisci_in_lista(&lista, valore_inserito);
	}

	stampa_lista(&lista);

	return 0;
}
