import threading
import time
threads1 = []

def sleeper(name, n):
    l1=[]
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    time.sleep(1)
    l1.append(name)
    l1.append(n)
    print('{} has woken up from sleep \n'.format(name))
    print(l1)
    time.sleep(1)
    print(threads1.append(l1))

start = time.time()

threads = []
nam=["Atul","Anand","Vikash","Chandan","Atharav"]
for i in range(0,len(nam)):
    t = threading.Thread(target=sleeper, name='thread{}'.format(i), args=(nam[i], 'thread{}'.format(i)))
    threads.append(t)
    t.start()
    print('{} has started \n'.format(t.name))


for i in threads:
    i.join()

print(threads1)
end = time.time()

print('time is {}'.format(end - start))




