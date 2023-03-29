#Pentru a incepe codul mai intai vom declara o lista cu numele A
#Folosind libraria random vom genera 10 numere cu valori intre 1 si 99
#Folosind extensia .append din list aceste 10 numere sunt inserate inapoi in lista
import random as rand
#Numim variabilul listei "Array" si il declaram *[]* gol pentru a insera valorile folosind modulul random
Array = []
amount = 10
for k in range(amount):
    Array.append(rand.randint(1, 99))
#Aici avem functia ce contine un mic algoritm de sortare cu interschimbare
#Functia face "return" la valorile sortate din lista random numita Array
def sort_schimb(array_sort_schimb):
    # Aici puteti sa vedeti un for loop care analizeaza lenghth-ul listei suv variabilul Array
    for i in range(len(Array)):
        #Pozitia unu de search va fi declarata cu vairabilul iter_min cu pozitia i declarata mai sus in for loop
        iter_min = i
        #Aici declaram inca un for loop pentru a declara conditiile pentru interschimbarea valorilor
        for j in range(i + 1, len(Array)):
            #Daca pozitia minima din lista "Array" este mai mare sau egal cu pozitia maxima "j"
            #Atunci declaram iter_min ca fiind j adica in acest caz toata lista a fost analizata
            if Array[iter_min] >= Array[j]:
                iter_min = j
        #Aici aplicam conditiile interschimbarii de sortare, schimband valoare mai mica cu valoarea mai mare
        #Comparam 2 valori din lista pana cand ajungem la pozitia maxim j din lista "Array
        Array[i], Array[iter_min] = Array[iter_min], Array[i]
    #Declaram aplicatie ca dorim sa returnam valoarea listei "Array" sortate sub variabilul "array_sort_list"
    return array_sort_schimb
#Dam ca output lista nisortata cu valorile din lista random "Array" pentru a putea testa daca alogritmele de mai jos functioneaza corect
print("Lista nesortata:", Array)
#Aici lasam user-ul sa aleaga ce numar doreste sa gaseasca in lista Array
#Lista in acest caz este inca nesortata
cap_liniar_nesortat = int(input("Alegeti numarul pe care vreti sa-l gasiti in lista folosind search liniar nesortat"))
#Declaram functia pentru algoritmul de search liniar pentru lista Array nesortata
def linear_search_nesortat(array_sort_liniar_nesortat, cap):
    #Declaram pozitia minim i ca fiind 0 pentru
    i = 0
    #Declaram un while loop pentru a stabili conditiile de min max in acest algoritm de search
    while i < len(array_sort_liniar_nesortat):
        #Aici aplicam conditia pentru algoritmul de search
        #Daca punctul 0 din lista "Array nesortat" este egal cu --->
        if array_sort_liniar_nesortat[i] == cap:
            #--->Atunci Aici declaram pozitia valorii cerute de catre user in variabilul "cap_liniar_nesortat"
            globals()["pozitia"] = i
            #Dam return la valoarea True pentru a da output la "Gasit" si pozitia unde a fost gasita valoarea
            return True
        #Iterare pozitia pana se gaseste valoarea, Increment position variabil with +1 each time
        i += 1

if linear_search_nesortat(Array, cap_liniar_nesortat):
    print("Gasit la pozitia", pozitia + 1)
else:
    #In caz ca vloarea data de catre user nu este gasit output ---> Null
    print("Null")

array_sort = sort_schimb(Array)
print("Lista sortata", array_sort)
#Dam ca output cel mai mare numar intreg din lista Array
#Acesta sa gaseste gasind ultimu termen dat n din lista -1 "n-1" sau intr-o lista n[-1]
print("Numarul cel mai mare este: ", max(Array))
#User input for cap_liniar_sortat
cap_liniar_sortat = int(input("Alegeti numarul pe care vreti sa-l gasiti in lista folosind search liniar sortat"))
#Aceeasi functie ca si functia anterioara
#Search liniar doar ca in acest caz lista Array a fost sortata
def linear_search_sortat(array_sort_liniar_sortat, cap):
    i = 0

    while i < len(array_sort_liniar_sortat):
        if array_sort_liniar_sortat[i] == cap:
            globals()["pozitia"] = i
            return True
        i += 1

if linear_search_sortat(array_sort, cap_liniar_sortat):
    print("Gasit la pozitia", pozitia + 1)
else:
    print("Null")
#Userul alege valoarea pe care doresc sa o gaseasca in lista Array
cap_binar = int(input("Alegeti numarul pe care vreti sa-l gasiti in lista folosind search binar"))
#Functia de sortare binara
def binary_search(array_sort_binar, cap_binar_local):
    #Declaram pozitia cea mai mica din lista sortata Array
    lower = 0
    #Declaram pozitia cea mai mare din lista sortata Array
    upper = len(array_sort_binar) - 1
    '''
    Aplicam conditiile pentru searchul binar
    Searchul binar cere ca lista "Array" sa fie impartita in doua jumatatati ce vor fi verificate
    In acesta caz folosim pozitiile upper si lower pentru a simplifica algoritmul 
    Algoritmul de search merge cel mai bine intr-o lista sortata iar intr-o lista nesortata mai ales in python dureaza
    Mult-nu este indeajuns de eficient pentru o lista nesortata
    '''
    while upper >= lower:
        mid_list = (upper + lower) // 2
        if array_sort_binar[mid_list] == cap_binar_local:
            globals()["pozitia"] = mid_list
            return True

        elif array_sort_binar[mid_list] < cap_binar_local:
            lower = mid_list
        else:
            upper = mid_list

if binary_search(array_sort, cap_binar):
    print("\nNumarul a fost gasit la pozitia: ", pozitia + 1)
else:
    #Daca numarul nu a fost gasit output ---> "Numarul nu a fost gasit"
    print("Numarul nu a fost gasit!: ")

#Arbitrary function to display ascending and descending List
def sortare_main():
    print("Lista sortata crescator: ")
    for cresc in range(len(Array)):
        print(Array[cresc], end=" ")
    print("\nLista sortata descrescator: ")
    rev_array = Array[::-1]
    for desc in range(len(rev_array)):
        print(rev_array[desc], end = " ")
sortare_main()
#Program End