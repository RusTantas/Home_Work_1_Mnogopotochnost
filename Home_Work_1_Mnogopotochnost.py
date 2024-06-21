from threading import Thread
import time

def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1)

if __name__ == "__main__":
    thread1 = Thread(target=print_numbers)
    thread2 = Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()




# from threading import Thread, Semaphore
# import time
#
# number_semaphore = Semaphore(1)
# letter_semaphore = Semaphore(0)
#
# def print_numbers():
#     for i in range(1, 11):
#         number_semaphore.acquire()
#         print(i)
#         letter_semaphore.release()
#         time.sleep(1)
#
# def print_letters():
#     for letter in 'abcdefghij':
#         letter_semaphore.acquire()
#         print(letter)
#         number_semaphore.release()
#         time.sleep(1)
#
# if __name__ == "__main__":
#     thread1 = Thread(target=print_numbers)
#     thread2 = Thread(target=print_letters)
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()
#
