import multiprocessing
import random
import timeit
import time

def sorting_thread(array, pid) :
    
    print('#############Thread #%d started...............\n' %pid)

    start = timeit.default_timer()
    random_function(array)
    sorting_function(array)
    print_array(array, pid)
    stop = timeit.default_timer()
    print('%0.3f sec' %(stop-start))
        
def random_function(array):
    i=0
    for i in range(10):
        array[i]=random.randrange(0,100)
    return    

def sorting_function(array) :
    i=9
    for i in range(9,0,-1):
        j=0
        for j in range(i):
            time.sleep(0.01)
            if array[j] > array[j+1] :
                tmp = array[j+1]
                array[j+1]=array[j]
                array[j]=tmp
    return            

def print_array(array, pid):
    print"[%d] --> "  %pid,; 
    for i in range(10):
        print"%d " %array[i],;

if __name__ =='__main__' :
    array=multiprocessing.Array('i',[0]*10)
    print('############Start#############')
    
    for i in range(10) :
        p = multiprocessing.Process(target=sorting_thread, args=(array, i))
        p.start()
    p.join()
    print('#############End###############')

    '''
    Output
############Start#############
#############Thread #0 started...............

#############Thread #1 started...............

#############Thread #2 started...............

#############Thread #3 started...............

#############Thread #4 started...............

#############Thread #5 started...............

#############Thread #7 started...............

#############Thread #6 started...............

#############Thread #8 started...............

#############Thread #9 started...............

[2] -->  5  9  15  24  27  30  65  72  87  91  0.493 sec
[1] -->  5  9  15  24  27  30  65  72  87  91  0.495 sec
[0] -->  5  9  15  24  27  30  65  72  87  91  0.496 sec
[3] -->  5  9  15  24  27  30  65  72  87  91  0.497 sec
[5] -->  5  9  15  24  27  30  65  72  87  91  0.500 sec
[9] -->  5  9  15  24  27  30  65  72  87  91  0.496 sec
[4] -->  5  9  15  24  27  30  65  72  87  91  0.501 sec
[6] -->  5  9  15  24  27  30  65  72  87  91  0.498 sec
[7] -->  5  9  15  24  27  30  65  72  87  91  0.499 sec
[8] -->  5  9  15  24  27  30  65  72  87  91  0.498 sec
#############End###############
    '''
