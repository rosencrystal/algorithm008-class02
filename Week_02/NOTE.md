学习笔记

# 1 哈希表 Hash Map
* 定义

    哈希表（Hash table），也叫散列表，是根据关键码值（Keyvalue）而直接进行访问的数据结构。

    它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。

    这个映射函数叫作散列函数（Hash Function），存放记录的数组叫作哈希表（或散列表）。

* 应用
    * 缓存（LRU Cache）
    * 键值对存储（Redis）

* 特点
    * 存在哈希碰撞，解决方法之一是 拉链式解决冲突法
    * 查询、插入、删除在通常情况下时间复杂度都是O(1)
    * 最坏的情况下可能退化成链表，那是上面三个时间复杂度都变成O(n)   

* 在python中的表现形式
    * 键值对 dict
    * 集合   set    


---

# 2 树 Tree
树其实是链表的升维版本，链表是特殊化的树，树是特殊化的图

# 3 二叉树 Binary Tree
* python示例：
```
class TreeNode:
    def __init__(self, val):
    self.val = val
    self.left, self.right = None, None
```
* 二叉树遍历
    * 前序遍历（pre-order）： 根-左-右

    * 中序遍历（in-order）：  左-根-右

    * 后序遍历（post-order）：左-右-根
  

 ```
 class TreeNode:
    def __init__(self,val):
        self val = val
        self.left, self.right = None, None

class Tree:
    def __init__(self, root: TreeNode):
        self.traverse = []
        self.root = root

    def preorder(self, root)        
        if root:
            self.traverse.apend(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root)        
        if root:
            self.inorder(root.left)
            self.traverse.apend(root.val)
            self.inorder(root.right)

    def postorder(self, root)        
        if root:
            self.postorder(root.left)
            self.postorder(root.right)  
            self.traverse.apend(root.val)    
 ```   

# 4 二叉搜索树 Binary Search Tree
二叉搜索树，也称二叉搜索树、有序二叉树（Ordered Binary Tree）、排序二叉树（Sorted Binary Tree），是指一棵空树或者具有下列性质的二叉树：
1. 左子树上所有结点的值均小于它的根结点的值；
2. 右子树上所有结点的值均大于它的根结点的值；
3. 以此类推：左、右子树也分别为二叉查找树。 （这就是 重复性！）

**中序遍历：升序排列** 

Demo: https://visualgo.net/zh/bst


# 5 堆 Heap
可以快速找到一堆数中最大或最小值得数据结构。

如果根节点是最大值叫大顶堆，根节点是最小值叫小顶堆。

常见的操作时间复杂度：
* find-max: O(1)
* delete-max: O(logN)
* insert(create): O(logN) or O(1)

不同实现的比较：https:/ /en.wikipedia.ora/wiki/HeaP_(data_structure) 

# 6 二叉堆
通过完全二叉树来实现的堆（注意不是二叉搜索树）。

## 6.1 性质
* 是一颗完全树
* 任意父节点的值总是大于等于其子节点的值

## 6.2 实现细节
* 二叉堆一般都是通过“数组”来实现
* 假设第一个元素在数组中的索引为0，那么任意节点i和它的父节点及子节点的位置关系如下：
    1. 左子节点的索引是 **2*i+1**
    2. 右子节点的索引是 **2*i+2**
    3. 父节点的索引是 **floor((i-1)/2)**

## 6.3 操作  
* insert O(logN)
    1. 新元素一律放在堆的尾部
    2. 依次向上调整整个堆的结构直到根节点 HeapifyUp
* delete-max O(logN)
    1. 将堆尾元素替换到堆顶，移除堆尾元素
    2. 依次从根部向下调整整个堆的结构直到堆尾 HeapifyDown   




