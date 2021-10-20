def citire_lista():
    l =[]
    givenString = input("Introduceti lista de numere intregi separate prin virgula: ")
    numbersAsString = givenString.split(',')
    for i in numbersAsString:
        l.append(int(i))
    return l


def same_nr_elemente_pare(l1, l2):
    '''
    
    :param l1: prima multime de numere intregi  
    :param l2: a doua multime de numere intregi
    :return: True daca au acelasi numar de elemente pare si False daca nu
    '''

    nr1=0
    nr2=0
    for x in l1:
        if x % 2 == 0:
            nr1+=1
    for x in l2:
        if x % 2 == 0:
            nr2+=1
    if nr1 == nr2:
        return True
    else:
        return False


def intersectia_multimilor(l1,l2):
    '''

    :param l1: prima multime de numere intregi
    :param l2: a doua multime de numere intregi
    :return: lista noua reprezentand intersectia celor 2 multimi date de la tastatura
    '''

    l = [] #intersectia celor 2 multimi
    l=[x for x in l1 if x in l2]
    return l




def test_same_nr_elemente_pare():
    assert same_nr_elemente_pare([1,2,4,5], [7,8,9,10]) == True
    assert same_nr_elemente_pare([1, 2, 4, 6,8], [7, 8, 9, 10]) == False
    assert same_nr_elemente_pare([1, 2, 4, 5,10], [7, 8, 9, 10,8]) == True


def test_intersectia_multimilor():
    assert intersectia_multimilor([1,2,3,4,5,], [2,3,9]) == [2,3]
    assert intersectia_multimilor([3, 4, 5,19,20], [2, 7, 9]) == []
    assert intersectia_multimilor([19,20,7,5,], [19,99,201]) == [19]




def main():
    test_same_nr_elemente_pare()
    test_intersectia_multimilor()
    l1 = []
    l2 = []
    while True:
        print("1.Cititi cele 2  liste de numere intregi ")
        print("2.Afișați dacă cele două liste au același număr de elemente pare ")
        print("3.Afisati intersectia celor 2 multimi")
        print("a.Afisati cele 2 liste de numere intregi ")
        print("x.Exit ")
        optiune = input()
        if optiune =='1':
            l1=citire_lista()
            l2=citire_lista()
        elif optiune =='2':
            print(same_nr_elemente_pare(l1,l2))
        elif optiune == '3':
            print(intersectia_multimilor(l1,l2))
        elif optiune == 'a':
            print(l1)
            print(l2)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida, va rog reincercati ")

if __name__ == "__main__":
    main()
