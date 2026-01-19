MOD = 1000000007

def max_subarray_product(arr):
    n = len(arr)
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for i in range(1, n):
        if arr[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(arr[i], max_prod * arr[i])
        min_prod = min(arr[i], min_prod * arr[i])
        
        result = max(result, max_prod)
    
    return result % MOD

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + N]))
        index += N
        
        result = max_subarray_product(arr)
        results.append(result)
    
    for res in results:
        print(res)


solve()