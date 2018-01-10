.rdata
	#DIM è una parola di 4 byte con un solo elemento che mi indica la lunghezza dell'Array
	DIM:
		.word 10

.data
	#A è un array di 10 elementi
	A:
		.word 1 4 6 10 45 68 29 9 18 10

.text
.globl main

main:  
	
	#Calling convenction - Call setup
	
	addi sp, sp, -8
	sw fp, 4(sp)
	sw ra, 0(sp)
	move fp, sp
	
	la $a0, A #Carico in a0 l'indirizzo base di Array
	la $a1, DIM #Carico in a1 l'indirizzo base di DIM
	lw $a1, 0($a1) #Carico in a1, l'elemento contenuto in DIM, cioè 10 nel nostro caso
	
	jal somma_lista #salto alla funzione #Salto alla funzione

	#Calling convenction - Return cleanup
	
	move sp, fp
	lw ra, 0(sp)
	lw fp, 4(sp)
	addi sp, sp, 8
	 
	jr $ra

somma_lista:   	#Calling convenction - Call setup
	
				addi sp, sp, -8
				sw fp, 4(sp)
				sw ra, 0(sp)
				move fp, sp

				#a0 = indirizzo base del vettore
				#a1 = numero di elementi della lista
				#t0 = contatore elementi
				#t1 = somma degli elementi
				
				addi $t0, $t0, 1 #Sommo al contatore degli elementi 1 in quanto sto accedendo al primo file
				slt $t2, $a1, $t0 #Controllo che a1, cioè il numero degli elementi, sia minore dell'elemento al quale sto accedendo
				bne $t2, $zero, exit #Nel caso in cui sto accedendo ad un indicice che supera la lunghezza dell'Array, salto ad exit
				lw $t2, 0(a0) # Carico l'elemeto della lista
				add t1, t1, t2 # Sommo l'elemento alla somma dei precedenti
				j prossimo_elemento
				
prossimo_elemento: addi $a0, $a0, 4 #Sommo 4 all'indirizzo base per accedere all'elemento successiv
					j somma_lista #Salto a somma_lista, cioè rieseguo la procedura
				
exit:  				move $v0, $t1 #Copio in $vo il contenuto di $t1, cioè il risultato che mi interessa

					#Calling convenction - Return cleanup
					#Ripristino lo Stack
					move sp, fp
					lw ra, 0(sp)
					lw fp, 4(sp)
					addi sp, sp, 8
	 
					Restituisco il controllo al chiamante
					jr $ra

				
				