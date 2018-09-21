import redis

conn = redis.Redis(host='192.168.1.88')
print('Washer is starting')
dishes = ['salad', 'bread', 'entree', 'dessert']
#num  = 1
for dish in dishes:
    msg = dish.encode('utf-8')
    conn.rpush('dishes', msg)
    print('Washed', dish)
    #num += 1
conn.rpush('dishes', 'quit')
print('Washer is done')