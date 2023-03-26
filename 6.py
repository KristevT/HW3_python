def IsSymmetric():
    n = int(input())
    cnt = 0 # счётчик
    matrix = []
    for i in range(n):
        row = list(map(int, input().split())) # ввод матрицы 
        matrix.append(row)
    d_num = matrix[n-1][0] # число в начале диагонали (слева снизу) - с этим числом мы будем сравнивать все последующие числа на диагонали

    for j in range(n):
        if matrix[n-1-j][j] == d_num: # сравнивание тех самых чисел
            cnt += 1 # пополнение счётчика при совпадении чисел

    return n == cnt

print(IsSymmetric())