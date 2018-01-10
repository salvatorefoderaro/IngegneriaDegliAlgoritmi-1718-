





char *concatenaStringa (char *stringa_uno, char *stringa_due, char *nuova_stringa){
		
		char *copia_stringa_uno;
		char *copia_stringa_due;
		
		for (copia_stringa_uno = stringa_uno; *copia_stringa_uno != '\0'; ++copia_stringa_uno){
			*nuova_stringa = *copia_stringa_uno;
			++nuova_stringa;
		}
		
		for (copia_stringa_due = stringa_due; *copia_stringa_due != '\0'; ++copia_stringa_due){
			*nuova_stringa = *copia_stringa_due;
			++nuova_stringa;
		}
		
		return nuova_stringa;
		
		
	}


#include <stdio.h>
#define L 3


int controllo_stringa(char *stringa){
	
	char *copia_stringa;
	int len = 0;
	for (copia_stringa = stringa; *copia_stringa != '\0'; ++copia_stringa){
		if (*copia_stringa == ' '){
				len = 0;
			}
		
		if (len > L){
			return 1;
		}
		else{
		len = len + 1;
		}
	}
	return 0;
};

void stampa_stringa(char *stringa){
	
	char *copia_stringa;
	for (copia_stringa = stringa; *copia_stringa != '\0'; ++copia_stringa){
		printf("%c", *copia_stringa);
	}
	
}




int main(void){
	
	char *s = "Stringa";
	char *p = "Cio a ttt";
	
	stampa_stringa(s);
	printf("\n");
	stampa_stringa(p);
	printf("%d", controllo_stringa(s));
	printf("\n%d", controllo_stringa(p));
	
	return 0;
}