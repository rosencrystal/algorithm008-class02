学习笔记
# 第1周 数组、链表、跳表、栈、队列
## 1. 数组
* prepend   O(1)   
* append    O(1)
* looup     O(1)
* insert    O(N)
* delete    O(N)
---
## 2. 链表
* prepend   O(1)   
* append    O(1)
* looup     O(N)
* insert    O(1)
* delete    O(1)
---
## 3. 跳表

跳表是多级链表，用来优化单链表的读取速度的

跳表查询的时间复杂度是O(logN), 空间复杂度是O(N)

查询速度得到了很大的提高，但是相应的增加了维护数据结构的复杂度

---
## 4. 栈
特点：FILO，先进后出，可以类比子弹匣

操作：
* looup     O(N)
* pop       O(1)
* push      O(1)
---
## 5. 队列
特点：FIFO，先进先出，可以类比食堂排队

操作：
* looup     O(N)
* pop       O(1)
* push      O(1)

---
## 6. 优先级队列

队列的变种，比较具有实用性，可以类比生活中军人或残疾人优先的队列

特点：底层具体实现的数据结构较为多样和复杂：heap， bst， treap

操作：
* pop       O(logN)
* push      O(1)

---
## 7. 双端队列
可以简单理解为两端都可以进的队列

操作：
* pop       O(1)
* push      O(1)

Python的代码实现:
```
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.deque = []
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque) == self.capacity:
            return False
        else:
            self.deque.insert(0, value)
            return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque) == self.capacity:
            return False
        else:
            self.deque.append(value)
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque) == 0:
            return False
        else:
            self.deque.pop(0)
            return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque) == 0:
            return False
        else:
            self.deque.pop()
            return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.deque) == 0:
            return -1
        else:
            return self.deque[0]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.deque) == 0:
            return -1
        else:
            return self.deque[-1]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.deque) == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.deque) == self.capacity
```