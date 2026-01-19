def solve():
  N, p0, T = input().split()
  N = int(N)
  p0 = float(p0)
  T = int(T)

  l = [input().split() for _ in range(N)]
  prices = [0] * (N)
  cnt = 1 # 가격을 제시하고 있는 로봇의 수 (초기 1번 로봇만 가격 제시)
  prices[0] = p0 # 1번 로봇의 초기 가격 설정

  # 1일부터 T-1일까지 시뮬레이션 (T일 아침 가격이 목표이므로)
  for i in range(1, T):
    # 이전 날짜(i-1)의 가격들을 기준으로 현재 평균 계산
    avg = sum(prices) / cnt if cnt > 0 else 0

    # 각 로봇에 대해 가격 갱신 여부 확인
    for idx in range(N):
      start_date, interval, margin_rate = l[idx]
      start_date = int(start_date)
      interval = int(interval)
      margin_rate = float(margin_rate)

      # 현재 날짜(i)가 로봇의 시작일 이후이고, 갱신 간격에 해당하는 날짜인 경우
      if i >= start_date and (i - start_date) % interval == 0:
        # 이 로봇이 이전에 가격을 제시한 적이 없다면 (가격이 0이라면)
        if prices[idx] == 0:
          cnt += 1 # 활성화된 로봇 수 증가
        
        # 새로운 가격 계산 및 반올림 (소수점 둘째 자리까지)
        prices[idx] = round(avg * (1 + margin_rate), 2)
  
  # 최종 가격 출력 (소수점 둘째 자리까지)
  for price in prices:
    print(f"{price:.2f}")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()