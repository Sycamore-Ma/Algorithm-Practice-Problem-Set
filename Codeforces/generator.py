with open("input.txt", "w") as f:
    # 生成一个 超长的 大写字母字符串
    f.write("20\n")
    for i in range(20):
        for j in range(10000):
            f.write(chr(65 + i % 26))
        f.write("\n")