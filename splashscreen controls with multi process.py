import time
from multiprocessing import Process
import splashscreen
def sp():
 splashscreen.splash_screen()


if __name__=="__main__":

    p=Process(target=splashscreen.destroy)
    p1=Process(target=sp)
    print('p1 started')
    p1.start()
    time.sleep(2)
    print('p started')
    p.start()
    p.join()
    p1.join()
    print('hi')

