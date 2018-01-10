.data

	Stringa1:
		.asciiz 
		
	Stringa2:
		.asciiz
	L: # Contiene il numero massimo della lunghezza delle singole parole
		.word

#.bss
	
	Stringa3:
		.space x
		
		
.text
.globl main

concatenate_string_control_lenght:

	# a0 indirizzo base Stringa1 (*first)
	# a1 indirizzo base Stringa2 (*second)
	# a2 indirizzo base Stringa3 (*new)
	# a3 = L (3 in questo caso)
	# to lunghezza prima stringa (*len_first)
	# t1 lunghezza seconda stringa (*len_second)
	# v0 = 0 return OK
	# V0 = 1 return ERROR
	
	addi sp, sp, -8
	sw ra, 4(sp)
	sw fp, 0(sp)
	move fp, sp
	
	add t0, zero, zero
	add t1, zero, zero
	
loop_stringa1:		
	
	lw t2, 0(a0) # *first
	nop
	beq t2, '0', fine_parola1 # *first == '0' esci dal ciclo
	nop
	sw t2, 0(a2) # *new = *first
	addi a0, a0, 4 # ++first
	addi a2, a2, 4 # ++new
	addi t0, t0, 1 # ++len_first
	j loop_stringa1 # Torna nuovamente nel ciclo
	nop
	
fine_parola1:

	slt t4, t0, a3 # len_first < L?
	beq t4, zero, exit_errore # len_first > L -> break
	nop
	j loop_stringa2 # passa al ciclo successivo
	nop

loop_stringa2:

	lw t2, 0(a1) # *second
	nop
	beq t2, '0', fine_parola2 # *second == '0' esci dal ciclo
	nop
	sw t2, 0(a2) # *new = *second
	addi a1, a1, 4 # ++second
	addi a2, a2, 4 # ++new
	addi t1, t1, 1 # ++len_second
	j loop_stringa2 # Torno nuovamente nel ciclo
	nop
	
fine_parola2:
	
	slt t4, t1, a3 # len_second < L?
	beq t4, zero, exit_errore # len_second > L? -> break
	nop
	j termina_nuova_stringa # aggiungo il terminatore alla nuova stringa e concludo

termina_nuova_stringa:

	lw '0', 0(a2) # *new = '0'
	j exit_ok #
	nop

exit_errore:

	addi v0, zero, 1 # v0 = 1 -> Errore come avevo definito io sopra
	
	move sp, fp
	sw fp, 0(sp)
	sw ra, 4(sp)
	add sp, sp, 8
	
	jr ra # restituisco il controllo
	nop
	
exit_ok:
	
	add v0, zer0, zer0 # v0 = 0 -> Corretto come avevo definito prima
	
	move sp, fp
	sw fp, 0(sp)
	sw ra, 4(sp)
	add sp, sp, 8
	
	jr ra # restituisco il controllo
	nop
	
main:

	addi sp, sp, -8
	sw ra, 4(sp)
	sw fp, 0(sp)
	move fp, sp
	
	la a0, Stringa1 # a0 = indirizzo prima stringa
	la a1, Stringa2 # a1 = indirizzo seconda stringa
	la a2, Stringa3 # a2 = indirizzo nuova stringa 
	la a4, L # a4 = indirizzo base vettore singola parola
	nop
	lw a4, 0(L) # a4 = contenuto di L (3 nel nostro caso)
	
	jal concatenate_string_control_lenght
	
	move sp, fp
	lw fp, 0(sp)
	lw ra, 0(sp)
	addi sp, sp, 8
	
	jr ra
	nop

	
	
	
	