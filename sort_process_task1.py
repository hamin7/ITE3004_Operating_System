import multiprocessing
import random
import timeit
import time

def sorting_thread(array, pid) :
    
    print('#############Thread #%d started...............\n' %pid)

    start = timeit.default_timer()          # start the timer.
    random_function(array)          # function that randomly pick 10 numbers.
    sorting_function(array)         # function that sort numbers.
    print_array(array, pid)         # function that print sorted numbers.
    stop = timeit.default_timer()       # stop the timer.
    print('%0.3f sec' %(stop-start))        # time to sort.
        
def random_function(array):
    i=0
    for i in range(10):
        array[i]=random.randrange(0,100)        # randomly pick the number in range 1~100.
    return    

def sorting_function(array) :
    i=9
    for i in range(9,0,-1):
        j=0
        for j in range(i):
            time.sleep(0.01)            # in order to slow down.
            if array[j] > array[j+1] :      # swap the bigger one and smaller one.
                tmp = array[j+1]
                array[j+1]=array[j]
                array[j]=tmp
    return            

def print_array(array, pid):
    print"[%d] --> "  %pid,;            # print the process's id. 
    for i in range(10):
        print"%d " %array[i],;              # print sorted numbers.

if __name__ =='__main__' :
    array=multiprocessing.Array('i',[0]*10)
    print('############Start#############')
    
    for i in range(10) :
        p = multiprocessing.Process(target=sorting_thread, args=(array, i))     # p is multiprocessing thread.
        p.start()       # start the work.
    p.join()        # stop the work.
    print('#############End###############')
