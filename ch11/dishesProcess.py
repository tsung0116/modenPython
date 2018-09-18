import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print('Drying', dish, 'dish')
        input.task_done()

if __name__ == '__main__': 
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()
    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)
    dish_queue.join()


# An attempt has been made to start a new process before the
# current process has finished its bootstrapping phase.
# This probably means that you are not using fork to start your
# child processes and you have forgotten to use the proper idiom
#        in the main module:
#
#            if __name__ == '__main__':
#                freeze_support()
#                ...
#
#        The "freeze_support()" line can be omitted if the program
#        is not going to be frozen to produce an executable.