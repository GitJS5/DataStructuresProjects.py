'''
Folosind acest program o sa aratam cum functioneaza un model de lista inlantuita in Python
Fata de programul anterior de sortare si gasire, aici folosim "class" pentru a putea pasa mai usor variabilele din alte
functii:Importam modulul random sub numele prescurtat rand pentru a insera mai tarziu valorile in lista inlantuita
'''
import random as rand
class Main:
    #Cream functia de initializare a Nodurilor din sir.
    def __init__(self, data, nextNod=None):
        self.data = data
        self.next = nextNod

class LinkedList:
    #Aici avem functia de initializare default python ce returneaza valoarea self folosita in clasele python
    #Ii atribuim valoare "head"/cap
    def __init__(self):
    #Head este folosit pentru a retine pozitia valorii din lista in LinkedList
    #Functioneaza foarte similar cu variabilul "cap" din aplicatia anterioara "BinaryLinkedSearch"
        self.head = None

    # Mai adaugam o functie ca sa inseram un nou nod la inceput.
    #Aceasta functie o folosim si la finalul aplicatiei pentru a insera valori noi in sir
    def inserare(self, info):
        nod_nou = Main(info)
        nod_nou.next = self.head
        self.head = nod_nou


     #Avand o referinta la capul unei liste si o cheie,
     #stergem prima aparitie a cheii din lista legata
    def stergere(self, key):
    #Declaram un variabil numit temp pentru a tine valoarea din selg
        temp = self.head
     #Aici aplicam conditia
        while temp is not None:
            if temp.data == key:
                break
            #Stabilim o pozitia anterioara pentru un output complet cand inseram valorile in lista
            prev = temp
            #Temp continua cu urmatoarea pozitia din lista
            temp = temp.next

        # Imi punem o conditie cu if temp = None, daca key nu era prezenta in lista inlantuita.

        if temp is None:
            return

    # Scoatem nodul de la lista inlantuita.
        prev.next = temp.next


    #Aici declaram functia "printList"
    #Functia print lista ne va arata outputul listei inlantuite
    def printList(self):
        temp = self.head
        while temp:
            print(" %d" % (temp.data),"->" ,end=" "),
            temp = temp.next
            if temp.next is None:
                print('Stop')
                break

amount = int(input("Va rog alegeti lungimea dorita pentru lista inlantuita"))
#Aici se declara valorile ce le vom punem in lista inlantuita liniara
link_array = LinkedList()
#Declaram variabilul lin_array pentru a face referinta la clasa "LinkedList" din linia 7
#Vom aplica metoda "random" din aplicatia anterioara "BinaryLinearSearch" pentru a avea un rezultat imparţial
link_array.inserare("Stop")
for i in range (amount):
    link_array.inserare(rand.randint(1,9))
#Aici printam lista creata cu valorile date
print("Lista creata: ")
link_array.printList()
link_array.stergere(rand.randint(1,9))
print("Outputul listei inlantuite dupa ce am sters o valoare: ")
link_array.printList()
