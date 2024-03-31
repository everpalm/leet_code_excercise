from threading import Semaphore

class Foo:
    def __init__(self):
        self.runSecond = Semaphore(0)
        self.runThird = Semaphore(0)
        # pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.runSecond.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.runSecond.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.runThird.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.runThird.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()