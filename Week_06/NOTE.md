学习笔记
#  动态规划
## 1 回忆递归和分治
* 递归模板
```
def recur(level, param):
    # terminator
    if (level > max_level): return

    # current level logic
    process(level, param)

    # drill down
    recur(level + 1, param)

    # restor status
    #ToDO
```

* 分治模板
```
def device_conquer(problem, param1, param2, ...):
    # terminator 
    if not problem:
    print result
    return

    # prepare data
    data = prepare_data(problem)
    subproblems = splib_problem(problem, param)

    # conquer subproblems
    subresult1 = device_conquer(subproblems[0], p1, p2, ...)
    subresult2 = device_conquer(subproblems[1], p1, p2, ...)
    subresult3 = device_conquer(subproblems[2], p1, p2, ...)

    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3)

    # revert the current level states
    # ToDO

```

* 心得
1. 不要人肉递归, 不仅低效而且很可能是错的
2. 找到最近最简方法, 将其拆解成可重复解决的问题 -> 最重要
3. 数学归纳法思维
4. 找重复性的根本原因是计算机只会傻傻的for, while

## 2 什么是动规
* 动规 = 分治 + 最优子结构   
* 关键点:动规与递归或分治其实没有根本性的区别, 关键是看有没有最优子结构(max, min或其他特殊限制条件)
2. 共性:找到重复子问题
3. 差异性:最优子结构, 中途可以淘汰次优解
4. 尝试将解决问题的思路从自顶向下变成自底向上

## 3. 动规模式
1. define最优子结构, 这是最难的点, 只有通过多做题目熟悉这类问题   
opt[n] = best_of(opt[n-1], opt[n-2], ...)

2. 状态空间  opt[i]

3. DP方程: 其实就是最有子结构的代码化   
Fib: opt[i] = opt[n-1] + opt[n-2]
2D-path: opt[i,j] = opt[i+1][j] + opt[i][j+1] (根据a[i][j]是否是障碍物进行剪枝)


## 4. 动规小结
1. 打破自己的思维惯性，形成机器思维(我是个没有感情的刷钱机器)

2. 理解复杂逻辑的关键(最优子结构,开始可以套模板)

3. 也是职业进阶的要点要领(主要思想还是分治)

