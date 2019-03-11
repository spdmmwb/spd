task2Machines = []
task3Machines = []


with open('dane.txt') as f:
    w1, h1 = [int(x) for x in next(f).split()]
    for line in f:
        task2Machines.append([int(x) for x in line.split()])




with open('dane2.txt') as f:
    w2, h2 = [int(x) for x in next(f).split()]
    for line in f:
        task3Machines.append([int(x) for x in line.split()])




starttime = []
def Permutation2Machines(table,indeks):
    if indeks < len(table):
        for i in range(indeks, len(table)):
            table[i], table[indeks]  = table[indeks], table[i]
            Permutation2Machines(table, indeks+1)
            table[i], table[indeks]  =  table[indeks], table[i]
    else:
        print(table)
        st1 = 0
        st2 = table[0][0]
        et1 = st1 + table[0][0]
        et2 = st2 + table[0][1]
        for index in range(1, len(table)):
            st1 = et1
            st2 = max(et2, et1)
            et1 = st1 + table[index][0]
            et2 = st2 + table[index][1]

        print("Czas wykonania operacji: " + str(et2))



def takelower(table):
    length = len(table)
    if table[length-2] >= table[length-1]:
        return table[length-1]
    else:
        return table[length-2]

def Johnson2(table):
    table.sort(reverse = True, key=takelower)
    solution = []
    for i in range(0,len(table)):
        if table[i][0]>table[i][1]:
            solution.append(table[i])
        else:
            solution.insert(0,table[i])
    print("\nJohnson 2 maszyny:")
    print(solution)



def Permutation3Machines(table,indeks):
    if indeks < len(table):
        for i in range(indeks, len(table)):
            table[i], table[indeks]  =  table[indeks], table[i]
            Permutation2Machines(table, indeks+1)
            table[i], table[indeks]  =  table[indeks], table[i]
    else:
        print(table)
        st1 = 0
        starttime[0].append(st1)
        st2 = table[0][0]
        starttime[1].append(st2)
        et1 = st1 + table[0][0]
        et2 = st2 + table[0][1]
        st3 = et2
        starttime[2].append(st3)
        et3 = st3 + table[0][2]

        for index in range(1, len(table)):
            st1 = et1
            starttime[0].append(st1)
            st2 = max(et2, et1)
            starttime[1].append(st2)
            et1 = st1 + table[index][0]
            et2 = st2 + table[index][1]
            st3 = max(et3, et2)
            starttime[2].append(st3)
            et3 = st3 + table[index][2]

        print("Czas wykonania operacji: " + str(et3))

def Johnson3(table):
    for index in range(0, len(table)):
        table[index].append(table[index][0] + table[index][1])
        table[index].append(table[index][1] + table[index][2])

    table.sort(reverse=True, key=takelower)
    solution = []
    for i in range(0, len(table)):
        if table[i][3] > table[i][4]:
            solution.append(table[i])
        else:
            solution.insert(0, table[i])

    for table in solution:
        del table[4]
        del table[3]

    print("\nJohnson 3 maszyny:")
    print(solution)
Permutation2Machines(task2Machines, 0)
Johnson2(task2Machines[:])
print("-------------------------------------")
Permutation3Machines(task3Machines,0)
Johnson3(task3Machines)