*Relazione progetto*

**Ingegneria degli Algoritmi – AA 2017 2018 – Prima Prova in Itinere**

**Studente:** Foderaro Salvatore

**Numero di Matricola:** 0214381

**Problema - Binary search tree con lazy deletion**

**Descrizione algoritmo**

Per l’implementazione del dizionario, ho da prima definito la funzione
**lazyInsert**, identica alla funzione **insert** già presente nel
dizionario degli alberi binari, con l’unica differenza nell’aggiunta del
terzo campo nella lista delle informazioni del nodo, impostato di
default a 0. Ho definito questo terzo elemento della lista come **Valore
di eliminazione del nodo**; se uguale a 1, il nodo risulta eliminato.

Ho inoltre definito le seguenti funzioni aggiuntive:

-   **deletionValue(nodo):** restituisce il valore di eliminazione del
    nodo

-   **setDeleted(nodo):** segna il nodo come eliminato, andando ad
    impostare ad 1 il valore di eliminazione

-   **setUnDeleted(nodo):** segna il nodo come non eliminato, andando ad
    impostare a 0 il valore di eliminazione

-   **isDeletedOr(nodo):** restituisce True se il nodo risulta
    eliminato, altrimenti False

-   **setValue(nodo,valore**): permette di modificare il valore di un
    nodo

Per la risoluzione del problema ho definito le funzioni richieste:

1.  **lazySearch(chiave):** cerco il nodo associato alla chiave e
    controllo se è segnato come eliminato. In caso negativo, restituisco
    il nodo, altrimenti restituisco None

2.  **boolDeleteLazy(chiave):** tramite **lazySearch** cerco il nodo
    associato alla chiave. Se la funzione chiamata restituisce il nodo,
    quindi quest’ultimo è presente nell’albero e non è segnato come
    eliminato, allora segno il nodo come eliminato e restituisco True.
    Altrimenti, nel caso in cui **lazySearch** restituisce None, dunque
    il nodo non è presente nell’albero o è presente ma risulta come
    eliminato, restituisco False

3.  **insertLazyControl(chiave,valore):** prima di inserire la coppia
    (chiave, valore) nell’albero, controllo se esiste già un nodo
    associato alla chiave che voglio inserire e controllo se
    risulta eliminato. In caso positivo, tramite **setValue** imposto il
    valore passato alla funzione come nuovo valore del nodo e lo segno
    come non eliminato. Nel caso in cui invece non è presente
    nell’albero nessun nodo associato alla chiave, o quest’ultimo
    risulta non eliminato, effettuo il normale inserimento tramite
    **lazyInsert**

**Utilizzo Lazy Deletion**

L’uso della Lazy Deletion è preferibile nei casi in cui dopo
l’eliminazione di un nodo, è molto probabile il suo reinserimento,
oppure quando si vuole indicare un nodo come “disabilitato”. Utilizzando
la Lazy Deletion, invece di rimuovere il nodo e dopo doverlo reinserire,
semplicemente lo segno come eliminato. Al reinserimento del nodo,
l’operazione mi costerà solo l’aggiornamento dell’informazione relativa
all’eliminazione, ed al massimo l’aggiornamento dell’informazione
relativa al suo valore.
