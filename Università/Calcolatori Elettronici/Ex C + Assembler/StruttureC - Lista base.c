#include <stdio.h>

/* Creo una struttura nodo con due attributi:
	1) Intero v;
	2) Indirizzo next;
	
	Piccola parentesi sul punto 2:
	
	Abbiamo detto che *next significa che next deve essere un indirizzo, in questo caso l'indirizzo del nodo successivo.
	Bisogna specificare "struct node *next", in quanto in C bisogna indicare la natura ed il tipo di qualsiasi oggetto.
	Cioè in questo modo stiamo dicendo al programma che:
	
	1) In next sarà presente un indirizzo
	2) !!! Cosa importante !!! L'indirizzo presente in C deve essere associato ad una struttura del tipo node.
	
	In modo ancora più banale:
	
	NON POSSO ASSOCIARE A NEXT L'INDIRIZZO DI UN TIPO DI DATO DIFFERENTE, COME UN INTERO, UN CARATTERE O ALTRO
	
	Fare attenzione, perché la parte ostica del C è proprio questa.
	
	*/
	

struct esame {

    int v;
    struct node *next;
};



void insert_after_node(struct node *p, struct node *n){
	
/* Tramite questa funzione, inserisco il nodo p dopo il nodo n */

/* Dovendo inserire il nuovo elemento dopo il nodo p, implica che il nodo p aveva un successore.
   Quindi, quello che vado a fare è:
   
   1) Il nodo a cui puntava p->next, cioè il successore di p, diventa ora il successore del nuovo nodo n che abbiamo inserito */
n->next = p->next;

/* 2) Il nodo successivo di p, in quanto vogliamo inserire n dopo p, sarà proprio n  */
p->next = n;

/* Sottolineo come p->next deve contenere un indirizzo, ed infatti andiamo ad assegnagli n che, ricordiamo, è l'indirizzo del nodo da inserire! */
};

void stampa_lista(struct node *nodo_iniziale){
	
/* Tramite questa funzione procedo alla stampa della lista.
   Utilizzo un puntatore di appoggio p, a cui associo l'indirizzo di nodo_iniziale, cioè il nodo che ho passato alla funzione
   
   */
   
  


  a {100, &b} -> b {101,&c} -> c {102,NULL} -> NULL

stampa_lista(&a) ==  
	
struct node *p;
	
for (p=nodo_iniziale; p != NULL; p=p->next){
	
	/* Eseguo il ciclo for, con p = nodo iniziale. Fin quando il valore di p->next, cioè il nodo successivo della lista
	   sarà diverso da NULL (va visto come uno zero), allora stampo l'elemento p->v, che rappresenta il valore del nodo nel nostro caso.
	   Il "p=p->next" ci permette di accedere ad ogni esecuzione del ciclo al nodo successivo. */
	
	
   printf("Valore di p %d", p->v);
}


}

int main(void){
	
/* Definisco i diversi nodi, nella forma {valore_nodo, nodo_successivo}  */

struct node d = {6, NULL};
struct node c = {5, &d};
struct node b = {4, &c};
struct node a = {3, &b};


struct node g = {50, NULL};

/* Come al solito, la funzione stampa_lista deve ricevere in input un indirizzo, quindi le passo l'indirizzo di a. */
stampa_lista(&a);

/* Anche in questo caso passo alla funzione gli indirizzi dei due nodi */
insert_after_node(&b, &g);

return 0;
}
