li =[]

def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]

    print(lena)
    print(lenb)
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'up'
    return c, flag


def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'ok':
        printLcs(flag, a, i - 1, j - 1)
        # print a[i - 1]
        li.append(a[i-1])
    elif flag[i][j] == 'left':
        printLcs(flag, a, i, j - 1)
    else:
        printLcs(flag, a, i - 1, j)

def exec():
    # a = 'ARWQRQBCBDASFJIOAAB'
    # b = 'BDREQWTRCWABQRQWRQWRTYKOEQPA'
    # a = 'ac'
    # b = 'acb'
    a = [180, 180, 141, 146, 141, 200, 235, 235, 173, 141, 141, 172, 180]
    b = [165, 235, 180, 141, 240, 171, 173, 172]
    c, flag = lcs(a, b)
    printLcs(flag, a, len(a), len(b))
    print(li)
    ratio = 1 - len(li)/min(len(a),len(b))
    print(ratio)

if __name__ == '__main__':
    exec()



# #a、b表示两个mac在某段时间内的轨迹id序列

# 可以学习下递归
# up:表名 当前行对应元素无匹配节点，开始判断i-1行元素的匹配关系
# left：表明当前列对应元素无匹配节点，开始判断j-1列元素的匹配关系
# 当前函数属于穷举类型的，但复杂度还行，具体多少不会算