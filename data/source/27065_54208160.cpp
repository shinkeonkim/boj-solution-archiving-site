#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll D[5500] = {0, 1}; // 자기 자신을 제외한 약수의 합
ll T, N;

ll f(int n) {
	ll ret = 1;
	
	for(int i = 2; i * i <= n; i++) {
		if(n % i) continue;
	
		if(i * i == n) ret += i;
		else ret += i + n / i;
	}
	
	return ret;
}

void init() {
	for(int i = 2; i <= 5000; i++) {
		D[i] = f(i);
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> T;
	
	init();
	
	while(T--) {
		cin >> N;
		
		bool chk = true;
		
		if(D[N] <= N) chk = false;
		
		for(int i = 2; i * i <= N && chk; i++) {
			if(N % i) continue;
			
			if(D[i] > i) chk = false;
			if(D[N / i] * i > N) chk = false;
		}
		
		cout << (chk ? "Good Bye" : "BOJ 2022") << "\n";
	}
}