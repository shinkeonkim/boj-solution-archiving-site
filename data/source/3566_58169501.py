def f(a, b):
    return a // b + (1 if a % b else 0)
r_h, r_v, s_h, s_v = map(int, input().split())

ans = 987654321000
for i in range(int(input())):
    r_h_i, r_v_i, s_h_i, s_v_i, p = map(int, input().split())
    
    ans = min(ans, p * max(f(r_h, r_h_i), f(s_h, s_h_i)) * max(f(r_v, r_v_i), f(s_v, s_v_i)))
    ans = min(ans, p * max(f(r_h, r_v_i), f(s_h, s_v_i)) * max(f(r_v, r_h_i), f(s_v, s_h_i)))
    
    
print(ans)
