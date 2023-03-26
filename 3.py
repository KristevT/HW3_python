arr = list(map(int, input().split()))
last = arr[len(arr)-1] # запоминается последний элемент списка
for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1] # смещение всех элементов, кроме первого, вправо на одну позицию
arr[0] = last # замена первого элемента
print(*arr)
