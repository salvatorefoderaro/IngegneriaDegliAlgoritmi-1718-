.data

	vettore:
		.word 		# indirizzo base del vettore
	
	L:
		.word 10 # lunghezza massima
		
.text
.globl main

controllo_vettore:
	
	addi sp, sp, -8
	sw ra, 4(sp)
	sw fp, 0(sp)
	move fp, sp
	
	#a0 indirizzo base del vettore
	#a1 L
	#t0 copia indirizzo base del vettore
	#t1 contatore i
	
	slt t2, t1, a1
	beq t2, zero, termine_vettore
	nop
	
	/* Non esiste la terminologia vettore[i] come in C, quindi possiamo utilizzare
	   solamente i due metodi utilizzando gli indirizzi*/
	
	# Metodo 1
	
	lw t2, 0(a0) # *indirizzo_base
	addi a0, a0, 4	# ++indirizzo_base
	
	j controllo_vettore
	nop
	
	# Metodo 2
	
	sll t2, t1, 2 # offset i
	add t3, t0, t2 # indirizzo base + offset i
	nop
	lw t3, 0(t3) # *(indirizzo base + offset i)
	
	j controllo_vettore
	nop

termine_vettore:
	
	move sp, fp
	lw fp, 0(sp)
	lw ra, 4(sp)
	addi sp, sp, 8
	
	jr ra
	nop