a, b = map(int, input().split())

if a > 0 and b > 0:
    print("NorthEast")
elif a > 0 and b < 0:
    print("NorthWest")
elif a < 0 and b > 0:
    print("SouthEast")
elif a < 0 and b < 0:
    print("SouthWest")