#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

struct st {
	int idx, cost, back;
};

int N, K;
int cost[220000];
int back[220000];

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N >> K;
	
	back[N] = -1;

	for1(0, 220000) {
		cost[i] = 11000000;
	}

	queue<st> Q;
	
	Q.push({ N, 0, -1 });
	
	while(!Q.empty()) {
		st f = Q.front(); Q.pop();
		
		if(cost[f.idx] <= f.cost) continue;
		cost[f.idx] = f.cost;
		back[f.idx] = f.back;
		
		if(f.idx == K) break;
		
		if(f.idx != 0 && f.idx * 2 <= 100000 && cost[f.idx * 2] > f.cost + 1) {
			Q.push({f.idx * 2, f.cost + 1, f.idx });
		}

		if(f.idx + 1 <= 100000 && cost[f.idx + 1] > f.cost + 1) {
			Q.push({f.idx + 1, f.cost + 1, f.idx });
		}
		
		if(f.idx - 1 >= 0 && cost[f.idx - 1] > f.cost + 1) {
			Q.push({f.idx - 1, f.cost + 1, f.idx });
		}
		
	}
	
	cout << cost[K] << "\n";
	
	stack<ll> b;
	
	ll c = K;
	
	while(back[c] != -1) {
		b.push(c);
		c = back[c];
	}
	
	cout << N << " ";
	
	while(!b.empty()) {
		cout << b.top() << " ";
		b.pop();
	}
}