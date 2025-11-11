t = int(input())


contri = [-1] * 10000
pow_10 = [1]
for _ in range(20):
    pow_10.append(pow_10[-1] * 10)

# d 位数的所有加和贡献
def contribution_digits(d):
    if d < 0:
        return 0
    if contri[d] != -1:
        return contri[d]
    
    if d == 0:
        contri[d] = 0
    elif d == 1:
        contri[d] = 45
    else:
        # 最高位 0-9 10^{d-1} 次，其余末尾 0-9 9*10^{d-2} 次
        contri[d] = 45 * pow_10[d-1] + (d-1) * 45 * 9 * pow_10[d-2]
    return contri[d]


def prefix_dp_sum(n):
    if n < 0:
        return 0
    ans = 0
    pow = 1
    while pow <= n:
        next = n // (pow * 10)
        digit = (n // pow) % 10
        right = n % pow
        ans += next * 45 * pow
        ans += (digit * (digit - 1) // 2) * pow
        ans += digit * (right + 1)
        pow *= 10
    return ans


def range_sum(start, end):
    return prefix_dp_sum(end) - prefix_dp_sum(start - 1)

for _ in range(t):
    k = int(input())

    ans = 0
    d = 1
    cnt = 9

    while True:
        cnt = 9 * pow_10[d-1]
        block_len = d * cnt

        if k >= block_len:
            ans += contribution_digits(d)
            k -= block_len
            d += 1
        else:
            if d == 1:
                start = 1
            else:
                start = pow_10[d-1]
            num = k // d
            rem = k % d
            if num > 0:
                ans += range_sum(start, start + num - 1)
            if rem > 0:
                x = start + num
                for ch in str(x)[:rem]:
                    ans += int(ch)
            break

    print(ans)
