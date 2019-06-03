import time


task = []
readyToGo = []


def findBest(data, pivot, indexL, indexR):
    if len(task) == 0:
        return 0
    if task[0][0] > data:
        return 0
    if task[len(task) - 1][0] < data:
        return len(task)

    if indexL == pivot and (indexL + indexR) % 2 == 0:
        return (int)(indexL)
    if indexL == pivot and (indexL + indexR) % 2 == 1:
        return (int)(indexL + 1)
    if indexR == pivot and (indexL + indexR) % 2 == 0:
        return (int)(indexR)
    if indexR == pivot and (indexL + indexR) % 2 == 1:
        return (int)(indexR - 1)
    if task[pivot][0] <= data:
        return findBest(data, (int)(((pivot + indexR) / 2)), pivot, indexR)
    else:
        return findBest(data, (int)(((pivot + indexL) / 2)), indexL, pivot)


def insert(data):
    index = findBest(data[0], (int)(len(task) / 2), 0, len(task) - 1)
    task.insert(index, data)


def delete(currentTime):
    if len(task) > 0:
        if task[0][0] <= currentTime:
            item = task[0]
            del task[0]
            return item
    return None


######################
######################
######################
def findBestR(data, pivot, indexL, indexR):
    if len(readyToGo) == 0:
        return 0
    if readyToGo[0][2] < data:
        return 0
    if readyToGo[len(readyToGo) - 1][2] > data:
        return len(readyToGo)

    if indexL == pivot and (indexL + indexR) % 2 == 0:
        return (int)(indexL)
    if indexL == pivot and (indexL + indexR) % 2 == 1:
        return (int)(indexL + 1)
    if indexR == pivot and (indexL + indexR) % 2 == 0:
        return (int)(indexR)
    if indexR == pivot and (indexL + indexR) % 2 == 1:
        return (int)(indexR - 1)
    if readyToGo[pivot][0] >= data:
        return findBestR(data, (int)(((pivot + indexR) / 2)), pivot, indexR)
    else:
        return findBestR(data, (int)(((pivot + indexL) / 2)), indexL, pivot)


def insertR(data):
    index = findBestR(data[0], (int)(len(readyToGo) / 2), 0, len(readyToGo) - 1)
    readyToGo.insert(index, data)


def deleteR(currentEnd):
    try:
        max = 0
        for i in range(len(readyToGo)):
            if readyToGo[i][2] > readyToGo[max][2]:
                max = i
        item = readyToGo[max]
        if currentEnd < readyToGo[max][2]:
            del readyToGo[max]
            return item
        else:
            return None
    except IndexError:
        return None


machines = 0
tasks = 0

with open('dane.txt') as f:
    tasks, machines = [int(x) for x in next(f).split()]
    for line in f:
        insert([int(x) for x in line.split()])

currentTime = 0
currentElement = [0, 0, -1]
endTime = 0


while (len(task) > 0 or len(readyToGo) > 0 or currentElement != [0, -1, -1]):

    # Wyszukiwanie zadan gotowych do uzycia
    element = delete(currentTime)
    while element != None:
        insertR(element)
        element = delete(currentTime)

    # Sprawdzanie czy element sie zakonczyl
    if currentElement[1] == 0:
        if (endTime < currentElement[2] + currentTime):
            endTime = currentElement[2] + currentTime

        currentElement = [0, 0, -1]
    # Wybieranie aktualnego elementu
    currentEndTime = currentElement[2]
    bestEndIndex = 0

    useFlag = deleteR(currentEndTime)

    if useFlag != None:
        if currentElement[2] == -1:
            currentElement = useFlag
        else:
            insertR(currentElement)
            currentElement = useFlag
        useFlag = False

    currentElement[1] -= 1
    currentTime += 1


print(endTime)

# def delete(currentTime):
#    try:
#        max = 0
#        for i in range(len(task)):
#            if task[i][0] < task[max][0]:
#                max = i
#        item = task[max]
#        if task[max][0] <= currentTime:
#            del task[max]
#            return item
#        else:
#            return None
#    except IndexError:
#        return None

# def insertR(data):
#    readyToGo.append(data)

# def deleteR(currentEnd):
#    try:
#        max = 0
#        for i in range(len(readyToGo)):
#            if readyToGo[i][2] > readyToGo[max][2]:
#                max = i
#        item = readyToGo[max]
#        if currentEnd < readyToGo[max][2]:
#            del readyToGo[max]
#            return item
#        else:
#            return None
#    except IndexError:
#        return None