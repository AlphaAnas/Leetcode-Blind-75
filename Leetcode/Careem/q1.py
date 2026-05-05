def solution(values, K, L):
    n = len(values)
    for i in range(K, n):
        if values[i - K] == values[i]:
            return False
    return values[n - 1] <= L
