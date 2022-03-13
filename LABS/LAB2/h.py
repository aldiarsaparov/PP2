# def check(x0, y0, x, y):
#     distance = ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5
#     return round(distance, 3)


# x0, y0 = map(int, input().split())
# d = dict()
# lst = []

# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     point = str(x) + " " + str(y)
#     distance = check(x0, y0, x, y)

#     d[point] = d.get(point, distance)

# for key, value in sorted(d.items(), key=lambda x: (-x[1], x[0])):
#     lst.append(str(key))

# lst.reverse()

# print("\n".join(lst))