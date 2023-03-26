arr = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
n = int(input())
for i in range(0, n):
    print(arr[i-(i//5)*5])