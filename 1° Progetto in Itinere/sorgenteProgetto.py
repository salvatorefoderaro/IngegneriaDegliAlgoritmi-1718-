# coding: utf-8
"""
    File name: sorgenteProgetto.py
    Author: Salvatore Foderaro
    Date created: 16/11/2017
    Modified By: Salvatore Foderaro
    Date last modified: 30/11/2017
    Python Version: 2.7.14

    Questo modulo implementa le tre funzioni richieste dal primo problema della prima prova in Itenere AA 2017/2018:

    - bool delete(key k) è stata impelemntata con la funzione boolDeleteLazy
    - insert(key k, value v) è stata implementata con la funzione insertLazyControl
    - search(chiave k) è stata implementata con la funzione lazySearch
"""

from module.binaryTree import BinaryTree
from module.binaryTree import BinaryNode
from module.dictBinaryTree import DictBinaryTree

class DictLazy(DictBinaryTree):
    def __init__(self):
        self.tree=BinaryTree() # Le informazioni del nodo sono ora una tripla [key, value, lazyDelete]

    def deletionValue(self,node): 
        # Restituisce il valore di "eliminazione" del nodo (0 non eliminato, 1 eliminato)
        if node==None:
            return None #aiuta a calcolare il balance factor
        return node.info[2]

    def setDeleted(self,node):
        # Imposta il valore di eliminazione del nodo ad 1 (eliminato)
        if node == None:
            return None
        node.info[2] = 1
        
    def setUnDeleted(self,node):
        # Imposta il valore di eliminazione del nodo a 0 (Non eliminato)
        if node == None:
            return None
        node.info[2] = 0

    def isDeletedOr(self,node):
        # Controlla il valore di eliminazione del nodo. Ritorna True se il nodo è eliminato, mentre False se il nodo non è segnato come eliminato
        if node == None:
            return None
        elif self.deletionValue(node) == 0:
            return False
        else:
            return True

    def setValue(self,node,value):
        # Permette di impostare un valore preciso per un nodo
        if node == None:
            return None
        node.info[1] = value

    def setKey(self,node,newKey):
        # Permette di impostare una chiave specifica per un nodo
        if node == None:
            return None
        node.info[0] = newKey
    
    def lazySearch(self,key):
        """ search(chiave k) : Ritorna il nodo con chiave k se questo è
            presente nell’albero e non è segnato come eliminato. """
        
        node = self.searchNode(key)          # Cerco il nodo con la chiave che sto cercando
        if self.isDeletedOr(node) == False:  # Controllo che il nodo non sia impostato come eliminato
           return self.searchNode(key)       # Restituisco il nodo
        else:                                # Altrimenti non restituisco nulla
           return None
    
    def boolDeleteLazy(self,key):
        """ bool delete(key k) : Se il nodo con chiave k è presente nell’albero
            e non è segnato come “eliminato”, segna il nodo come eliminato e
            ritorna True. Se il nodo con chiave k non è presente nell’albero, o
            è presente ma è stato già precedentemente segnato come eliminato, ritorna False"""
        
        nodo = self.lazySearch(key)  # Trovo il nodo con valore key all'interno dell'albero
        if nodo != None:             # Controllo se il nodo con chiave k è presente nell'albero e se è segnato come eliminato o meno
           self.setDeleted(nodo)     # Segno il nodo come eliminato
           return True               # Restituisco True
        return False                 # Altrimenti restituisco False

    def insertLazyControl(self,key,value):
        """ Insert(key k, value v) : Inserisce una nuova coppia (k,v) nell’albero
            binario. Se è possibile inserire il nodo con chiave k nella posizione
            di un nodo segnato come eliminato, sostituisce il vecchio nodo con
            il nuovo. """
        maybeNode = self.searchNode(key)             # Cerco, se presente, un nodo con la stessa chiave key che sto cercando di inserire
        if self.isDeletedOr(maybeNode) == True:      # Controllo se già presente e se è impostato come eliminato
            # self.setKey(maybeNode, key)              # Nel caso in cui la condizione sia verificata, i
            self.setValue(maybeNode,value)           # Nel caso in cui la condizione sia verificata, copio il valore del vecchio nodo nel nuovo
            self.setUnDeleted(maybeNode)             # e lo imposto come non eliminato
        else:
            self.lazyInsert(key,value)               # Altrimenti procedo al normale inserimento
            

    def lazyInsert(self, key, value, lazyDelete=0):
        """Insert normale come visto a lezione, con l'unica differenza che oltre a key e value, è presente anche il nuovo valore lazyDelete.
           Se non indicato diversamente, il valore viene impostato a 0, cioè come non eliminato secondo il dizionario che ho impostato """
        pair = [key, value, lazyDelete]
        newt = BinaryTree(BinaryNode(pair))
        if self.tree.root == None:
            self.tree.root = newt.root
        else:
            curr = self.tree.root 
            pred = None             
            while curr != None:
              pred = curr
              if key <= self.key(curr): 
                  curr = curr.leftSon
              else:
                  curr = curr.rightSon
            if key <= self.key(pred):
                self.tree.insertAsLeftSubTree(pred, newt)
            else:
                self.tree.insertAsRightSubTree(pred, newt)

        
if __name__ == "__main__":
    albero = DictLazy() # Creo l'albero
    for i in range(1, 10):
        albero.lazyInsert(i, i)
    print("\nAlbero dopo inserimento elementi:")
    albero.tree.stampa() # Stampo l'albero
    albero.boolDeleteLazy(7)
    print("\nAlbero dopo boolDeleteLazy(7):")
    albero.tree.stampa() # Stampo l'albero dopo aver eseguito boolDeleteLazy
    print("\nChiamo lazySearch(7):")
    print albero.lazySearch(7)
    print("\nChiamo lazySearch(6):")
    print albero.lazySearch(6)
