# 所有叶子树链 最长公共子序列
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + [0] + p

    par = [0] * (n+1)
    kids = [[] for __ in range(n+1)]
    for i in range(1, n+1):
        if i == 1:
            # par[i] = 0
            continue
        else:
            par[i] = p[i]
        kids[par[i]].append(i)

    # 保证最短的就可以了，其他随便填
    depth = [0] * (n+1)

    def dfs(u, curDepth):
        depth[u] = curDepth
        for v in kids[u]:
            dfs(v, curDepth + 1)
    
    dfs(1, 1)


    # 统计深度桶

    maxDepth = max(depth)
    cnt = [0] * (maxDepth + 1)
    for u in range(1, n+1):
        cnt[depth[u]] += 1

    minDepth = 1000 + 1000
    # print(">>> depth", depth)
    for u in range(1, n+1):
        if not kids[u]:   # 找到了叶子节点
            minDepth = min(minDepth, depth[u])

    # print(ans)
    # # print(">>>", ans)

    # minDepth = ans

    ans = 0
    pref = [0] * (maxDepth+1)

    for d in range(1, maxDepth+1):
        pref[d] = pref[d-1] + cnt[d]


    # 从大到小枚举 level
    for level in range(minDepth, 0, -1):
        sumNodeCnt = pref[level]        # 前 level 层到根部的结点总数，其余为外层

        # 能否通过整层拼出来 x 个 0
        dp = [False] * (n + 1)      # dp[x] 前 level 层中选出若干层 x 个节点
        
        dp[0] = True

        for d in range(1, level + 1):
            currentDepthCnt = cnt[d]
            for x in range(sumNodeCnt, currentDepthCnt-1, -1):
                if dp[x - currentDepthCnt]:
                    dp[x] = True


        # 0 全部塞到外层：zeroNum >= k - (n-sumNodeCnt)
        # 1 全部赛到里层：zeroNum >= sumNodeCnt - (n-k)
        zeroNum_low = max(0, k - (n-sumNodeCnt), sumNodeCnt - (n-k))    # level 层里面至少要放这么多 0
        zeroNum_high = min(sumNodeCnt, k)                               # level 层里面最多最多也就放这么多 0

        if zeroNum_low <= zeroNum_high:
            ok = False
            for zeroNum in range(zeroNum_low, zeroNum_high+1):
                if dp[zeroNum]:
                    ok = True
                    break
            if ok:
                ans = level
                break

    print(ans)
    # print(">>>", ans)




# 反例：
# 1
# 4 2
# 1 1 1

# 0 0 1 1 没法分配
# 其实应该按照层数去涂色，是个 DP
# 不用考虑层数外面的零碎，这个层反正比下面分叉少，是最节省的方法了
