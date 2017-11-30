# coding=utf-8
"""
    File name: demoProgetto.py
    Author: Salvatore Foderaro
    Date created: 16/11/2017
    Modified By: Salvatore Foderaro
    Date last modified: 26/11/2017
    Python Version: 2.7.14

    Questo modulo implementa le sequenti funzioni:
	- dictLazyBench(number) crea un albero AVL con number-elementi ed esegue le tre funzioni implementate number-volte, stampando a video i singoli tempi di esecuzione
	- dictLazyGUI simula un esecuzione a video delle funzioni implementate in sorgenteProgetto.py
"""
from module.binaryTree import BinaryTree
from module.binaryTree import BinaryNode
from module.dictBinaryTree import DictBinaryTree
from sorgenteProgetto import *
import random
import time

def dictLazyBench(n):
    """La funzione mi permette di calcolare il tempo di esecuzione medio delle tre funzioni implementate nel nuovo dizionario"""
    print "\nTempo impiegato con ", n," valori"
    alb3 = DictLazy()
    for i in range (1,n):
        alb3.lazyInsert(random.randint(0,n*2),random.randint(0,n*2))

    start = time.time()
    for k in range (1,n):
        alb3.boolDeleteLazy(random.randint(0,n*2))
    end = time.time()
    elapsed = (end - start)
    print "Tempo boolDeleteLazy:", elapsed,"secondi"

    start = time.time()
    for j in range (1,n):
        alb3.lazySearch(random.randint(0,n*2))
    end = time.time()
    elapsed = (end - start)
    print "Tempo lazySearch:", elapsed,"secondi"

    start = time.time()
    for m in range (1,n):
        alb3.insertLazyControl(random.randint(0,n*2), random.randint(0,n*2))
    end = time.time()
    elapsed = (end - start)
    print "Tempo insertLazyControl:", elapsed, "secondi"


def dictLazyGUI():
    """La funzione mi permette di mostrare a video, a mo di interfaccia grafica, una Demo di esecuzione delle tre funzioni implementate"""
    print "\n                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          \n"

    print "Creo un Albero con le proprietà di Lazy Search ---------------> alb2 = DictLazy()  "
    print "Sfrutto un ciclo for per inserire 10 elementi nell'albero"
    alb2 = DictLazy()
    for i in range(1, 10):
        alb2.lazyInsert(i, i)
    print "\n                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< bool delete (key k) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          \n"
    print "=================== Funzione da implementare ==================="
    print "\nSe il nodo con chiave k e' presente nell albero e non e' segnato come eliminato, segna il nodo come eliminato e ritorna True.\nSe il nodo con chiave k non e' presente nell albero, o e' presente ma e' stato gia' precedentemente segnato come eliminato, ritorna False."
    print "\n=================== Demo implementazione ==================="
    node = alb2.searchNode(5)
    print "\nAssocio alla variabile node il nodo dell'albero con chiave 5 ---------------> node = alb2.searchNode(5)"
    print "Il nodo con chiave 5 e' segnato come eliminato? ------- alb2.isDeletedOr(node) --------> ", alb2.isDeletedOr(node)
    print "Cosa restituisce la funzione boolDeleteLazy(5)? ------- alb2.boolDeleteLazy(5) --------> ", alb2.boolDeleteLazy(5)
    print "Il nodo con chiave 5 e' segnato come eliminato? ------- alb2.isDeletedOr(node) --------> ", alb2.isDeletedOr(node)
    print "\nIl nodo con chiave 5 e' segnato come eliminato? ------- alb2.isDeletedOr(node) --------> ", alb2.isDeletedOr(node)
    print "Cosa restituisce la funzione boolDeleteLazy(5)? ------- alb2.boolDeleteLazy(5) --------> ", alb2.boolDeleteLazy(5)
    print "\nCosa restituisce la funzione boolDeleteLazy(50)? [Elemento non apparteente all'array] ------- alb2.boolDeleteLazy(50) -------->  ", alb2.boolDeleteLazy(50)
    print "\n                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< search (key k) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          \n"
    print "=================== Funzione da implementare ==================="
    print "\nRitorna il nodo con chiave k se questo è presente nell’albero e non è segnato come eliminato."
    print "\n=================== Demo implementazione ==================="
    node1 = alb2.searchNode(9)
    print "\nAssocio alla variabile node1 il nodo dell'albero con chiave 9 ---------------> node1 = alb2.searchNode(9)"
    print "Il nodo con chiave 9 e' segnato come eliminato? ------- alb2.isDeletedOr(node1) --------> ", alb2.isDeletedOr(node1)
    print "Cosa restituisce la funzione lazySearch(9)? ------- alb2.lazySearch(9) --------> ", alb2.lazySearch(9)
    print "\nImposto il nodo come eliminato ---------------> alb2.setDeleted(node1)"
    alb2.setDeleted(node1)
    print "\nIl nodo con chiave 9 è segnato come eliminato? ------- alb2.isDeletedOr(node1) --------> ", alb2.isDeletedOr(node1)
    print "Cosa restituisce la funzione lazySearch(9)? ------- alb2.lazySearch(9) --------> ", alb2.lazySearch(9)
    print "\nCosa restituisce la funzione lazySearch(100)? [Elemento non appartenente all'array] ------- alb2.lazySearch(100) -------->", alb2.lazySearch(100)
    print "\n                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Insert (key k, value v) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          \n"
    print "=================== Funzione da implementare ==================="
    print "\nInserisce una nuova coppia (k,v) nell’albero binario. Se è possibile inserire il nodo con chiave k nella posizione di un nodo segnato come eliminato, sostituisce il vecchio nodo co  il nuovo."
    print "\n=================== Demo implementazione ==================="
    node3 = alb2.searchNode(3)
    print "\nAssocio alla variabile node3 il nodo dell'albero con chiave 9 ---------------> node3 = alb2.searchNode(3)"
    print "Imposto il nodo con chiave 3 come eliminato ---------------> alb2.setDeleted(node3)"
    alb2.setDeleted(node3)
    print "Inserisco un nuovo elemento con chiave 3 e valore 200 ---------------> alb2.insertLazyControl(3, 200)"
    alb2.insertLazyControl(3, 200)
    print "Qual'è il valore del nuovo nodo, nella posizione del precedente? ------- alb2.value(node3) -------->", alb2.value(node3)
    print "\nAlbero con valore sostituito:"
    alb2.tree.stampa()
    node4 = alb2.searchNode(4)
    print "\nAssocio alla variabile node4 il nodo dell'albero con chiave 4 ---------------> node4 = alb2.searchNode(4)"
    print "Il nodo con chiave 4 è segnato come eliminato? ------- alb2.isDeletedOr(node4) --------> ", alb2.isDeletedOr(node4)
    print "Inserisco un nuovo elemento con chiave 4 e valore 157 ---------------> alb2.insertLazyControl(4, 157)"
    alb2.insertLazyControl(4, 157)
    print "\nAlbero con nuovo elemento inserito:"
    alb2.tree.stampa()
    print "\n                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Benchmark Tempo >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          \n"

if __name__ == "__main__":

    dictLazyGUI()
    dictLazyBench(10000)
    dictLazyBench(100000)
    dictLazyBench(1000000)


