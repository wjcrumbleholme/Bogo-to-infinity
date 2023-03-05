from random import shuffle
import time
start_time=time.time()


def makeNewList(length):
    global list_shuffled, list_of_num
    list_of_num = []
    list_of_num = list(range(1, length + 1))
    list_shuffled = list_of_num[:]
    shuffle(list_shuffled)

def alikeness():
    global total_alikeness
    total_alikeness = 0
    for i in range(0, len(list_shuffled) - 1):
        total_alikeness += abs(list_shuffled[i] - (i+1))
    print(total_alikeness)
    
def alikecol():
    global total_alikeness
    sumTotal = sum(list_of_num) 
    #lower quartile (25%)
    lq = sumTotal / 4
    mid = sumTotal / 2 
    uq = sumTotal / 4 * 3
    
    if total_alikeness > uq:
        print("red")
        pass
    elif total_alikeness > mid:
        print("yellow")
        pass
    elif total_alikeness > lq:
        print('green')
        pass
    else:
        print('gold')
        pass
    
            


current_list_length = 10
makeNewList(current_list_length)
alikeness()
alikecol()


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
alikecol()


#---TODO---
# Previous times for sort + 1
# Current time (stopwatch)
# Total running time
