##Reti combinatorie
Una **rete combinatoria** è una rele logica ad *n* ingressi (x1, x2, ..., xn) ed *m* uscite (y1, y2, ..., ym), tale che ad ogni combinazione degli ingressi corrisponde una ed una sola combinazione delle uscite.

###Procedimento completo di sintesi

1. Descrizione informale
2. Tabella di verità
3. Forma canonica
4. Espressione di costo minimo (Teorema di Shannon, mappe di Karnaugh)
5. Schema logico

###Decoder semplice
E' un rete con **N** ingressi e *p* uscite, con p=2^N. Legge di corrispondenza è che *"Ogni uscita riconosce uno ed un solo stato di ingresso, in particolare l'uscita j-sima (Zj) riconosce lo stato di ingresso in cui i bit sono la codifica di j in base 2."*

###Multiplexer
Un **multiplexer** è una rete con 2^(N)+N ingressi ed un sola uscita. La combinazione degli **N** ingressi detti *di controllo* viene usata per "selezionare" uno dei rimanenti 2^N ingressi da riportare in uscita.

###Demultiplexer
Un **demultiplexer** è una rete con N+1 ingressi e 2^N uscite. La combinazione degli N ingressi detti *di controllo* viene usata per "selezionare" l'uscita su cui riportare il valore in ingresso.