import copy
import datetime
import random
import math


machines = 0
tasks = 0

task = []
with open('dane.txt') as f:
    tasks, machines = [int(x) for x in next(f).split()]
    for line in f:
        task.append([int(x) for x in line.split()])

def takenumber(table):
    return table[len(table)-1]

def counttime(table, machines):
    m = []
    m.append(table[0][0])


    for machine in range(1,machines):
        m.append(m[machine-1]+table[0][machine])


    for index in range(1,len(table)):
        for machine in range(0,machines):
            if machine == 0:
                m[0] = m[0]+table[index][0]


            else:
                m[machine]=max(m[machine-1]+table[index][machine],m[machine]+table[index][machine])



    return m[machines-1]


#*******************************************************
#*******************************************************
#*******************************************************

def probability(C1,C2,T):
    if C2 >= C1:
        return 2.71828182846 ** ((C1 - C2) / T)
    else:
        return 1



def annealing():
    T0 = 100
    k = 1
    kmax = 500
    while 1e-10 < T0:
        ranNumber = random.randint(0, len(task) - 1)
        ranNumber2 = random.randint(0, len(task) - 1)

        Cmax1 = counttime(task,machines)

        #Insert
        #task.insert(ranNumber,task.pop(ranNumber2))

        task[ranNumber], task[ranNumber2]=task[ranNumber2], task[ranNumber]
        Cmax2 = counttime(task, machines)

        prob = probability(Cmax1,Cmax2,T0)

        if prob < random.uniform(0,1):
            #task.insert(ranNumber2, task.pop(ranNumber))
            task[ranNumber], task[ranNumber2] = task[ranNumber2], task[ranNumber]

        T0 *= 0.50
        #T0 *= k/kmax
        #k += 1

print(counttime(task,machines))
start = datetime.datetime.now()
annealing()
duration = datetime.datetime.now() - start
print(task)
print(duration)
print(counttime(task,machines))