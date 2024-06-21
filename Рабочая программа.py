

import threading
import time

def print_number(a, event_for_wait):
    if a == 1:
        for i in range(1, 11):
            print(i)
            time.sleep(2)


    else:
        for i in range(ord('a'), ord('g')+1):
            print(chr(i))
            time.sleep(3)


    # event_for_set.set()
    event_for_wait.wait()  # wait for event
    # event_for_wait.clear()



if __name__ == "__main__":
    e1 = threading.Event()

    t1 = threading.Thread(target=print_number, args=(1, e1))
    t2 = threading.Thread(target=print_number, args=(2, e1))
    t1.start()
    t2.start()

    t1.join()
    t2.join()


#
# e1 = threading.Event()
# e2 = threading.Event()
#
# # init threads
# t1 = threading.Thread(target=writer, args=(0, e1, e2))
# t2 = threading.Thread(target=writer, args=(1, e2, e1))
#
# # start threads
# t1.start()
# t2.start()
#
# e1.set() # initiate the first event
#
# # join threads to the main thread
# t1.join()
# t2.join()