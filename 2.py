n = int(input())
cnt = 1 # счётчик степени
arr = [0, 1] # начальный список
arr_alt = [] # список дубликат
while 2**cnt < n:
    cnt += 1 # подбор степени двойки - понадобится в генерации последовательности

for i in range(cnt-1): # генерация последовательности, длина будет равна 2^cnt
    arr_alt = [] # обнуление списка-дубликата после цикла ниже
    for j in range(len(arr)):
        if arr[j] == 0:
            arr_alt.append(1)
        elif arr[j] == 1:
            arr_alt.append(0) # генерация списка дубликата: копируется начальный список с заменой 1 и 0
    arr = arr + arr_alt # объединение нач. списка и списка-дубликата

txt = ''
for m in range(n):
    txt += str(arr[m]) #вывод конечной последовательности длиной в n
print(txt)