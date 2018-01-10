#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <math.h>

// Programma in C che mi permette, dato un numero in virgola mobile a singola precisione, di ottenere il corrispettivo numero in base 10

int main(int argc, char *argv[])
{
    int i = 0, mantissa = 0 , potenza = 0, a = 0, numeroDecimale = 0;
    int c = 0;
    float exp, esponente;
	
// Calcolo l'esponente
	
for (i=1; i<9; i++){
	if (argv[1][i] == '1'){
    	int potenza = pow(2,8-i);
	    c = c + potenza;
	}
}

// Calcolo la mantissa

for (i=9; i<32; i++){
	if (argv[1][i] == '1'){
     float a = pow(2,8-i);
     esponente = esponente + a;
	}
}

    // "Correggo" il valore della mantissa in quanto rappresentata per eccesso

	mantissa = c - 127;
    esponente = 1 + esponente;
	
	 printf("\nEsponente=%d\n", mantissa);
     printf("Mantissa=%f\n", esponente);
     numeroDecimale = esponente * (pow(2,mantissa));
	 
	 // Controllo il primo bit, e procedo al cambio del segno nel caso il suo valore sia 1
	 
     	if (argv[1][0] == '1'){
        numeroDecimale = numeroDecimale * (-1);
	}
     printf("Numero decimale=%d\n", numeroDecimale);
	 return 0;
}