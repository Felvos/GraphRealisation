import math
import time
import random


class Queue:
    _queue = []
    lenght = 0

    def __init__(self):
        self._queue = []

    def add(self, value):
        self._queue.insert(0, value)
        self.lenght += 1

    def show(self):
        for i in range(len(self._queue)):
            print(str(self._queue[i]), end=" ")
        print("\n")
    def pop(self):
        a = self._queue[self.lenght - 1]
        del self._queue[self.lenght - 1]
        self.lenght -= 1
        return a
    def swap(self, i1, i2):
        if i1 > i2:
            i1, i2 = i2, i1
        buffer_queue1 = Queue()
        buffer_queue2 = Queue()
        for i in range(self.lenght - i2):
            self.add(self.pop())
        buffer_queue1.add(self.pop())
        for i in range(i2 - i1 - 1):
            buffer_queue2.add(self.pop())
        buffer_queue1.add(self.pop())
        buffer_queue1.add(buffer_queue1.pop())
        self.add(buffer_queue1.pop())
        for i in range(i2 - i1 - 1):
            self.add(buffer_queue2.pop())
        self.add(buffer_queue1.pop())
        for i in range(i1 - 1):
            self.add(self.pop())

    def sort(self):
        last_index = self.lenght - 1
        step = self.lenght // 2
        while step > 0:
            for i in range(step, self.lenght, 1):
                j = i
                delta = j - step
                while delta >= 0 and self._queue[delta] > self._queue[j]:
                    self.swap(delta + 1, j + 1)
                    j = delta
                    delta = j - step
            step //= 2




def main():
    new_queue = Queue()
    ans = int(input("Введите длину очереди: "))
    for i in range(ans):
        # new_queue.add(int(input("Введите " + str(i) + "-й элемент очереди: ")))
        new_queue.add(random.randint(0, 10000))
    new_queue.show()
    start_time = time.time()
    new_queue.sort()
    final_time = time.time()
    print("Время работы программы: " + str(final_time - start_time))
    new_queue.show()
if __name__ == "__main__":
    main()

