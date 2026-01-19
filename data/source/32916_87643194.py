w, h = map(int, input().split())

if w % 2 == 0:
    two_1_cnt = w // 2
    three_cnt = 0
	
	
else:
    two_1_cnt = (w - 3) // 2
    three_cnt = 1
	
three_2_cnt = 1 # 2nd row
w2 = w - 3
if w2 % 2 == 1:
    three_2_cnt += 1

ans = (h // 2) * (three_cnt + three_2_cnt)

if h % 2:
    ans += three_cnt

print(ans)
	