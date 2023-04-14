from time import ctime,sleep
import multiprocessing

def talk(content,loop):
    for i in range(loop):
        print("start talk:%s %s" %(content,ctime()))
        sleep(2)
def write(content,loop):
    for i in range(loop):
        print("start write:%s %s" %(content,ctime()))
        sleep(3)
process = []
p1 = multiprocessing.Process(target=talk, args=('Hello 51zxw',2))
process.append(p1)
p2= multiprocessing.Process(target=write, args=('Life is short, You need Python',2))
process.append(p2)


if __name__ == '__main__':
    for t in process:
        t.start()
    for t in process:
        t.join()
    print('All thread!%s' %ctime())


