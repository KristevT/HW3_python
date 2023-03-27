def can_eat():
    x1, y1 = map(int, input('Координаты коня (через пробел): ').split())
    x2, y2 = map(int, input('Координаты другой фигуры (через пробел): ').split())
    return (x1-2==x2 and (y1-1==y2 or y1+1==y2)) or (x1-1==x2 and (y1-2==y2 or y1+2==y2)) or (x1+1==x2 and (y1-2==y2 or y1+2==y2)) or (x1+2==x2 and (y1-1==y2 or y1+1==y2))

print(can_eat())