# 计算组合数C（n， i） 优化计算过程
def cnil(n, i):
    if not (isinstance(n, int) and isinstance(i, int) and n >= i):
        print('n,i 必须为数字，且n要大于i')
        return
    result = 1
    Min, Max = min(i, n - i), max(i, n - i)
    for i in range(n, 0, -1):
        if i > Max:
            result *= i
        elif i <= Min:
            result /= i
    return result

print(cnil(6, 2))