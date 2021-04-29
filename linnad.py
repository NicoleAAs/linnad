def linnad(gorod,ludi):
    while True:
        r=int(input("Введите количество городов, которые хотите внести в список: "))
        for i in range(1,r+1):
            gorodd=input("Введите название города: ")
            if gorodd in goroda:
                print("Такой город уже есть в списке!")
                continue
            else:
                gorod.append(gorodd)
                people=int(input("Введите количество жителей в этом городе: "))
                ludi.append(people)
        break

def find(gorod,ludi):
    while True:
        poisk=input("\nВведите название города: ")
        if poisk in gorod:
            b=gorod.index(poisk)
            print(f"\nГород: {gorod[b]}\nКоличество жителей: {ludi[b]}")
        else:
            print("\nТакого города нет в списке!")
        break

def sortbyalphabet(gorod,ludi):
    a=dict(zip(gorod,ludi))
    b=sorted(a)
    k=0
    while k!=len(ludi):
        print(b[k],"-",a.get(b[k]))
        k+=1

def maximum(gorod,ludi):
    m=ludi.index(max(ludi))
    print(f"\nГустонаселенный город: {gorod[m]}\nКоличество жителей: {ludi[m]}")

def lessthan(gorod,ludi):
    less=int(input("Введите количество жителей: "))
    a=0
    if min(ludi)>less:
        print("\nТаких городов в списках нет!")
    else:
        for k in ludi:
            if less>k:
                print(f"\nГород: {gorod[a]}\nКоличество жителей: {ludi[a]}")
            a+=1

def delete(gorod,ludi):
    deletename=input("Введите название города: ")
    f=gorod.index(deletename)
    gorod.pop(f)
    ludi.pop(f)

goroda=[]
zhiteli=[]
linnad(goroda,zhiteli)
while True:
    print(f"\nГорода - {goroda}\nЖители - {zhiteli}")
    print("\n0 - Выход\n1 - Добавить ещё города\n2 - Узнать, сколько в городе жителей\n3 - Сортировка в алфавитном порядке городов\n4 - Самый густонаселенный город\n5 - Города, в которых жителей меньше указанного числа\n6 - Удаление города и его данных\n")
    v=int(input())
    if v==0:
        print("Выход из программы")
        break
    if v==1:
        linnad(goroda,zhiteli)
    if v==2:
        find(goroda,zhiteli)
    if v==3:
        sortbyalphabet(goroda,zhiteli)
    if v==4:
        maximum(goroda,zhiteli)
    if v==5:
        lessthan(goroda,zhiteli)
    if v==6:
        delete(goroda,zhiteli)
