.rdata

	#M è una parola che contiene il numero 3
	M:
		.word 3
	
.data
	#S è una stringa che contiene una frase
	S:
		.asciiz "Questa è una stringa di prova"
		
.text
.globl main

main:	
		#Alloco spazio sullo Stack
		addi sp, sp, -8
		sw ra, 4(sp)
		sw fp, 0(sp)
		move fp, sp
		
		la $a0, S #Carico in a0 l'indirizzo base di S
		la $a1, M #Carico in a1 l'indirizzo base di M
		lw $a1, 0($a1) #Carico sempre in a1 il valore di M (3 nel nostro caso)
		jal controllo_lunghezza #Chiamo la funzione "controllo_lunghezza"
		
		#Ripristino lo stack
		move sp, fp
		lw fp, 0(sp)
		lw ra, 4(sp)
		addi sp, sp, 8
		
		#Restituisco il controllo al chiamante
		jr $ra
		
controllo_lunghezza:	

		#a0 = Indirizzo base della stringa
		#a1 = Numero massimo di caratteri di una stringa
		#t0 = Contatore lunghezza della singola parola
		#t1 = Carattere termine stringa -> '0'
		#t2 = Carattere termine parola -> ' '
		#v0 = 0, programma terminato correttamente
		#v1 = 1, programma terminato con errore
		
		addi sp, sp, -8
		sw ra, 4(sp)
		sw fp, 0(sp)
		move fp, sp
		
		add t1, t1, ' ' #t1 = carattere terminatore stringa
		add t2, t2, '0' #t2 = carattere terminatore parola
		add t0, zero, zero #t0 = 0 -> Situazione iniziale del contatore
	
loop:	
		lb $t3, 0(a0) #Carico in $t3 il carattere in posizione i della stringa
		beq $t3, t1, termina_programma #Se arrivo alla fine della stringa, termino il programma
		beq $t3, t2, prossima_parola #Se il carattere successivo è uno spazio, passo a "prossima parola"
		addi t0, t0, 1 #Incremento il contatore della lunghezza di 1
		j prossimo_carattere
	
prossimo_carattere:
		addi a0, a0, 1 #Incremento il contatore base di 1 per accedere al carattere successivo della stringa
		j loop #Ritorno nel Loop
		
prossima_parola:
		slt t3, t0, a1 #Controllo se t0, cioè la lunghezza della parola attuale, è minore del massimo (3)
		beq t3, zero, exit_errore #Se la condizione di sopra non è vera, allora termino il programma con un errore
		addi a0, a0, 1 #Incremento l'indirizzo base
		add t0, zero, zero #Pongo il contatore della nuova parola a 0
		j loop #Torno nel loop
		
termina_programma:
		slt t3, t0, a1 #Controllo e t0, cioè la lunghezza della parola attuale, è minore del massimo (3)
		beq t3, zero, exit_errore #Se la condizione di sopra non è vera, allora termino il programma con errore
		
		add v0, zero, zero #Se è tutto corretto, allora imposto v0 = 0

		#Ripristino lo stack
		move sp, fp
		lw fp, 0(sp)
		lw ra, 4(sp)
		addi sp, sp, 8
		
		#Restituisco il controllo alla funzione chiamante
		jr ra
		
exit_errore:
		addi v0, zero, 1 #Imposto v0 = 1
		
		#Ripristino lo stack
		move sp, fp
		lw fp, 0(sp)
		lw ra, 4(sp)
		addi sp, sp, 8		
		
		#Restituisco il controllo alla funzione chiamante
		jr ra
		
		
		