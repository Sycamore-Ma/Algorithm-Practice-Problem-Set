n, k, s = map(int, input().split())

dictionary = {}

for i in range(k):
    str = input()
    dictionary[str] = i + 1

S = input()
P = ""

for i in range(len(S)):
    c = S[i]
    if P + c in dictionary:
        P += c
    else:
        dictionary[P + c] = k + 1
        k += 1
        print(dictionary[P], end=' ')
        P = c

print(dictionary[P], end='\n')
print(k)
for item in dictionary:
    print(item)