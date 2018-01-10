#include <stdio.h>
#define L 10

void controllo_vettore(int *vettore_interi){

int *vettore_copia;

vettore_copia = vettore_interi;

for (int i=0; i<L; ++vettore_interi){

printf("\n\nL'elemento in posizione i è %d", vettore_interi[i]);

printf("\nAvendo incrmentato l'indirizzo base (++vettore_interi), posso accedere all'elemento i sfruttando i puntatori in due modi diversi:");
printf("\n1) Incremento ogni volta l'indirizzo base vettore_interi (++vettore_interi) ed accedo all'elemento puntato, ottenendo %d", *vettore_interi);
printf("\n2) Utilizzando l'indirizzo base del vettore, gli sommo i, cioè l'offset che rappresenta l'elemento dell'array al quale voglio accedere *(vettore_copia + i): %d", *(vettore_copia + i));

/* Incremento "a parte" i in quanto nel ciclo for ho incrementato l'indirizzo base */
++i;

}
}


int main(void){

int vettore[L] = {1,2,3,4,5,6,7,8,9,10};

controllo_vettore(vettore);

return 0;

}


