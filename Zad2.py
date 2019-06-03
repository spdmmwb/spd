import copy
import datetime

import copy
import datetime
import random
import math


def takenumber(table):
    return table[len(table) - 1]


def countttime(table, machines):
    m = []
    m.append(table[0][0])

    for machine in range(1, machines):
        m.append(m[machine - 1] + table[0][machine])

    for index in range(1, len(table)):
        for machine in range(0, machines):
            if machine == 0:
                m[0] = m[0] + table[index][0]


            else:
                m[machine] = max(m[machine - 1] + table[index][machine], m[machine] + table[index][machine])

    return m[machines - 1]


machines = 0
tasks = 0

task = []
with open('dane2.txt') as f:
    tasks, machines = [int(x) for x in next(f).split()]
    for line in f:
        task.append([int(x) for x in line.split()])




def takenumber(table):
    return table[len(table)-1]

def counttime(table, machines,accelerationArray):
    m = []
    m.append(table[0][0])
    #koniec pracy poszczegolnej maszyny
    #Start pierwszego zadania

    for machine in range(1,machines):
        m.append(m[machine-1]+table[0][machine])


    for index in range(1,len(table)):
        for machine in range(0,machines):
            if machine == 0:
                accelerationArray[machine]=m[0] = m[0]+table[index][0]


            else:
                accelerationArray[machine]=m[machine]=max(m[machine-1]+table[index][machine],m[machine]+table[index][machine])



    return m[machines-1]



def neh(table, machines, task_amound):
    accelecationArray = machines*[None]
    for elements in table:
        sum = 0
        for element in elements:
            sum += element
        elements.append(sum)



    table.sort(reverse=True, key=takenumber)


    for element in table:
        del element[len(element) - 1]

    solution = []
    time = (int)
    best_index = (int)



    for element in table:
        if len(solution) == 0:
            solution.append(element)
        else:
            time = 0
            best_index = 0
            for index in range(0,len(solution)+1):
                solution.insert(index,element)
                if index == 0:
                    time = counttime(solution,machines,accelecationArray)
                else:
                    if index == len(solution):
                        for machine in range(0, machines):
                            if machine == 0:
                                accelerationArray[0] = accelerationArray[0] + element[0]
                            else:
                                accelerationArray[machine] = max(accelecationArray[machine - 1] + element[machine],
                                                                              accelecationArray[machine] + element[machine])

                    else:
                        current_time = counttime(solution,machines,accelecationArray)
                    if time>current_time:
                        best_index = index
                        time =current_time
                del solution[index]
            solution.insert(best_index,element)


            #MODYFIKACJA
            current_index_time = (int)
            last_used_item = best_index
            time = 99999
            item = []



            if len(solution) > 0:
                for element in range(0,len(solution)):
                    if element != last_used_item:
                        item = solution.pop(element)
                        current_index_time = counttime(solution,machines,accelecationArray)
                        if time > current_index_time:
                            best_index = element
                            time = current_index_time
                        solution.insert(element,item)


                time = counttime(solution, machines,accelecationArray)
                current_element = solution.pop(best_index)
                for index in range(0,len(solution)+1):
                    solution.insert(index, current_element)
                    current_index_time = counttime(solution,machines,accelecationArray)
                    if time > current_index_time:
                        best_index = index
                        time = current_index_time
                    del solution[index]

                solution.insert(best_index, current_element)



    print(solution)
    print(countttime(solution, machines))
    ####DEL

    # *******************************************************
    # *******************************************************
    # *******************************************************

    def probability(C1, C2, T):
        if C2 >= C1:
            return 2.71828182846 ** ((C1 - C2) / T)
        else:
            return 1

    def annealing():
        T0 = 10
        k = 1
        kmax = 500
        while 1e-10 < T0:
            ranNumber = random.randint(0, len(solution) - 1)
            ranNumber2 = random.randint(0, len(solution) - 1)

            Cmax1 = countttime(solution, machines)

            # Insert
            # task.insert(ranNumber,task.pop(ranNumber2))

            solution[ranNumber], solution[ranNumber2] = solution[ranNumber2], solution[ranNumber]
            Cmax2 = countttime(solution, machines)
            prob = probability(Cmax1, Cmax2, T0)

            if prob < random.uniform(0, 1):
                # task.insert(ranNumber2, task.pop(ranNumber))
                solution[ranNumber], solution[ranNumber2] = solution[ranNumber2], solution[ranNumber]

            T0 *= 0.23
            # T0 *= k/kmax
            # k += 1

    print(countttime(solution, machines))
    start = datetime.datetime.now()
    annealing()
    duration = datetime.datetime.now() - start
    print(solution)
    print(duration)
    print(countttime(solution, machines))







    #######
    print(counttime(solution,machines,accelecationArray))


start = datetime.datetime.now()

neh(task,machines,tasks)
duration = datetime.datetime.now() - start
print(duration)
#####################################
