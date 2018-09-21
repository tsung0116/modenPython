def dryer():
    import redis
    import os
    import time

    conn = redis.Redis(host='192.168.1.88')
    pid = os.getpid()
    timeout = 30
    print('Dryer process %s is starting' % pid)
    while True:
        msg = conn.blpop('dishes', timeout)
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val == 'quit':
            break
        print('%s: dried %s' % (pid, val))
        time.sleep(0.1)
    print('Dryer process %s is done' % pid)

import multiprocessing

DRYERS=3

if __name__ == '__main__':
    for num in range(DRYERS):
        p = multiprocessing.Process(target=dryer)
        p.start()