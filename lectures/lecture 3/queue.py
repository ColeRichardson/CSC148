class Queue:
    """a queue FIFO

    """
    def __init__(self):
        """initializes the queue, the end of the queue is end of the list

        """
        self._items = []

    def is_empty(self):
        """checks if the queue is empty

        :return:
        """
        if self._items == []:
            return True
        else:
            return False

    def enqueue(self, item):
        """ adds current item to the end of the queue

        :param item:
        :return:
        """
        self._items.append(item)

    def dequeue(self):
        """removes the first element from the queue
        and returns it.
        returns none if the queue is empty
        :return:
        """
        if self.is_empty():
            return False
        return self._items.pop(0)
