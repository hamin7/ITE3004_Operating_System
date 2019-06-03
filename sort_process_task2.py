import multiprocessing
import random
import timeit
import time

def sorting_thread(array, pid, lock) :
    
    print('############Thread #%d started...............\n' %pid)
    lock.acquire()
    start = timeit.default_timer()
    random_function(array)
    sorting_function(array)
    print_array(array, pid)
    stop = timeit.default_timer()
    print('%0.3f sec' %(stop-start))
    lock.release()
    
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
    lock = multiprocessing.Lock()
    for i in range(10) :
        p = multiprocessing.Process(target=sorting_thread, args=(array, i,lock))
        p.start()
    p.join()
    print('#############End###############')

    '''
    Output
############Start#############
############Thread #1 started...............

############Thread #0 started...............

############Thread #2 started...............

############Thread #3 started...............

############Thread #4 started...............

############Thread #5 started...............

############Thread #6 started...............
############Thread #7 started...............


############Thread #8 started...............

############Thread #9 started...............

[1] -->  0  20  24  25  34  52  58  71  83  88  0.494 sec
[0] -->  19  44  44  46  49  60  67  69  77  86  0.492 sec
[2] -->  7  25  33  35  53  53  67  86  95  96  0.491 sec
[3] -->  8  15  24  45  62  64  68  79  82  99  0.494 sec
[4] -->  12  44  51  58  60  80  87  89  90  94  0.499 sec
[5] -->  5  11  13  19  36  55  61  74  88  93  0.498 sec
[7] -->  0  3  4  6  30  42  61  69  87  95  0.495 sec
[6] -->  6  13  14  23  47  55  63  64  86  99  0.492 sec
[8] -->  3  10  11  30  34  53  59  66  81  89  0.498 sec
[9] -->  1  3  28  42  49  52  70  78  89  94  0.490 sec
#############End###############

    '''
