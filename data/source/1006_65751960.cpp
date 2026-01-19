#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define INF 1000000000

using namespace std;
typedef long long ll;
typedef vector <ll> llv1;

int tc;
int N, W;
ll ar[11000][2];
ll D[11000][4];

ll cost_value(ll a, ll b) {
	return a + b <= W ? 1 : 2;
}

ll check_cost_value(ll a, ll b) {
	return a + b <= W ? 1 : INF;
}

ll min_value (const llv1& V) {
	ll res = INF;
	foreach(V) {
		res = min(res, i);
	}
	return res;
}

void init_dp_array() {
	for1j(0, 4) {
		for1(0, N + 2) {
			D[i][j] = INF;
		}
	}
}

void fill_dp_array() {
	for1(1, N + 1) {
		D[i][0] = min_value({
			D[i][0],
			D[i - 1][0] + cost_value(ar[i][0], ar[i][1]),
			D[i - 1][1] + 1,
			D[i - 1][2] + 1,
			D[i - 1][3],
		});

		D[i][1] = min_value({
			D[i][1],
			D[i - 1][0] + 1 + check_cost_value(ar[i][0], ar[i + 1][0]),
			D[i - 1][2] + check_cost_value(ar[i][0], ar[i + 1][0]),
		});

		D[i][2] = min_value({
			D[i - 1][0] + 1 + check_cost_value(ar[i][1], ar[i + 1][1]),
			D[i - 1][1] + check_cost_value(ar[i][1], ar[i + 1][1]),
		});

		D[i][3] = D[i - 1][0] + check_cost_value(ar[i][0], ar[i + 1][0]) + check_cost_value(ar[i][1], ar[i + 1][1]);
	}
}

void print_array() {
	for1(0, N + 1) {
		for1j(0, 4) {
			cout << D[i][j] << " ";
		}
		cout << "\n";
	}
}


ll solve() {
	ll res = INF;
	
	cin >> N >> W;
	
	for1j(0, 2) {
		for1(1, N + 1) {
			cin >> ar[i][j];
		}
	}
	
	// 1칸과 N칸이 겹치는 경우가 없는 경우
	init_dp_array();
	D[0][0] = 0;

	fill_dp_array();
	res = min(res, D[N][0]);

	// 1칸과 N칸이 위, 아래 모두 겹치는 경우
	init_dp_array();
	// print_array();
	D[0][3] = check_cost_value(ar[1][0], ar[N][0]) + check_cost_value(ar[1][1], ar[N][1]);
	
	fill_dp_array();
	res = min(res, D[N - 1][0]);
	
	// 1칸과 N칸이 위만 겹치는 경우
	init_dp_array();
	D[0][1] = check_cost_value(ar[1][0], ar[N][0]);
	fill_dp_array();
	res = min_value({
		res,
		D[N - 1][2],
		D[N - 1][0] + 1,
	});
	
	// 1칸과 N칸이 아래만 겹치는 경우
	init_dp_array();
	D[0][2] = check_cost_value(ar[1][1], ar[N][1]);
	fill_dp_array();
	res = min_value({
		res,
		D[N - 1][1],
		D[N - 1][0] + 1,
	});
	
	return res;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
	
  cin >> tc;
  while(tc--) {
	cout << solve() << "\n";
  }
}
