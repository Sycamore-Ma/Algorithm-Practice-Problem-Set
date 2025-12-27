n, k = map(int, input().split())

card = list(map(int, input().split()))

cardPileA = card[:k]
cardPileB = card[k:]

cardAfterShuffle = []

topA = True
while cardPileA and cardPileB:
    if topA:
        cardAfterShuffle.append(cardPileA.pop(0))
    else:
        cardAfterShuffle.append(cardPileB.pop(0))
    topA = not topA

print(" ".join(map(str, cardAfterShuffle + cardPileA + cardPileB)))