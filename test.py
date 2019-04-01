'''def Cards(s,v,f):
    return s + v + f


suit = '1248'  # 0001 - Red, 0010 - Blue, 0100 - Green, 1000 - Yellow
form = '1248'  # 0001 - Triangle, 0010 - Cross, 0100 - Disk, 1000 - Square
value = '1248' # 0001 - 1, 0010 - 2, 0100 - 3, 1000 - 4
cards = [Cards(s, v, f) for s in suit for v in value for f in form]
cards = cards + ['151515', '151515']
print(cards)
print(len(cards))'''

print(bin(1)+bin(1))
