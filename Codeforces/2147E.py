import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        a = list(map(int, input().split()))

        OR = 0
        for x in a:
            OR |= x

        base = OR.bit_count()

        # 计算每一位从“0 -> 1”的最小代价
        costs = []
        for k in range(32):
            if (OR >> k) & 1:
                continue  # 已经是 1，不花钱
            need = 1 << k
            mod = 1 << (k + 1)
            best = None
            for x in a:
                r = x & (mod - 1)        # x % 2^(k+1)
                if r >= need:
                    cost = 0
                else:
                    cost = need - r
                if best is None or cost < best:
                    best = cost
                if best == 0:
                    break
            costs.append(best)

        costs.sort()
        pref = [0]
        for c in costs:
            pref.append(pref[-1] + c)

        
        print("len(pref) >>>", len(pref))

        # 回答询问
        out = []
        for _ in range(q):
            b = int(input())
            # 在前缀和里找最大的 idx，使 pref[idx] <= b
            # 等价于 upper_bound
            lo, hi = 0, len(pref) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if pref[mid] <= b:
                    lo = mid
                else:
                    hi = mid - 1
            print(">>>", base + lo)
if __name__ == "__main__":
    solve()
