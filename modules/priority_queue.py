from heapq import heappush, heappop


class PriorityQueue:

    def __init__(self):
        self.queue = []

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def enqueue(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def dequeue(self):
        try:
            min_val = 0
            it = 0
            for i in self.queue:
                if i[1] < self.queue[min_val][1]:
                    min_val = it
                it += 1
            item = self.queue[min_val]
            del self.queue[min_val]
            return item
        except IndexError:
            print()
            exit()
