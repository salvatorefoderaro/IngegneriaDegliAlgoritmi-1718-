#include <stdio.h>

void conta_vocali(char *stringa){
	
/* Accedo alla stringa come visto ed aumento il contatore "vocali" solamente se becco un carattere "a" */

int vocali;
for (vocali = 0; *stringa != '\0'; ++stringa){
	
	if(*stringa == 'a'){
		++vocali;
	}


}
	printf("Il numero delle a è %d", vocali);

}	




int main(void){
	
	char *parola = "Numero di aaaaaavocali";
	
	conta_vocali(parola);
	
	return 0;
}