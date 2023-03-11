from random import shuffle
from colorama import Fore, Back, Style
import time
# start_time=time.time()

def makeNewList(length):
    global list_shuffled, list_of_num
    list_of_num = []
    list_of_num = list(range(1, length + 1))
    list_shuffled = list_of_num[:]
    shuffle(list_shuffled)

def shuffleList (list):
    shuffle(list)

def alikeness(list1):
    total_alikeness = 0
    for i in range(0, len(list1) - 1):
        total_alikeness += abs(list_shuffled[i] - (i+1))
    alikecol(total_alikeness, list1)
    

def alikecol(total_alikeness, list1):
    sumTotal = sum(list_of_num) 
    lq = sumTotal / 100 * 25
    mid = sumTotal / 100 * 45 
    uq = sumTotal / 100 * 65
    
    #lower alikeness is better
    if total_alikeness > uq:
        print(Fore.RED + str(list1))
    elif total_alikeness > mid:
        print(Fore.YELLOW + str(list1))
    elif total_alikeness > lq:
        print(Fore.GREEN + str(list1))
    else:
        print(Fore.CYAN + str(list1))


def sortChecker(list1):
    sorted = False
    tries = 0
    while sorted == False:
        sorted = True
        for i in range(0, len(list1) - 1):
            if list1[i+1] < list1[i]:
                sorted = False
        tries += 1
        alikeness(list1)
        shuffleList(list1)
        print (tries)


current_list_length = 15
makeNewList(current_list_length)
t1 = time.time()
sortChecker(list_shuffled)
t2 = time.time()-t1
print(f"sortChecker took {t2} seconds")


# while True:
#     sort_start_time=time.time()
#     while list_shuffled != list_of_num:
#         makeNewList(current_list_length)
#         alikeness()
#     time_taken = time.time() - sort_start_time
#     print(list_of_num)
#     print(list_shuffled)
#     print("Time taken to sort list of length " + str(current_list_length) + " is " + str(time_taken))
#     current_list_length += 1
#     makeNewList(current_list_length)
        
makeNewList(10)

#---TODO---
# Previous times for sort + 1
# Current time (stopwatch)
# Total running time
