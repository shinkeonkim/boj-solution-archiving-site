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
	ll y, x, cost;
};

ll N, M;
ll D[110][110];
string ar[110];

int dy[] = { 0, 0, 1, -1 };
int dx[] = { 1, -1, 0, 0 };

const ll INF = 1000000LL;

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N >> M;
	
	for1(0, N) {
		cin >> ar[i];
	}
	
	memset(D, INF, sizeof(D));
	
	queue<st> Q;
	
	Q.push({0, 0, 1});
	
	while(!Q.empty()) {
		st here = Q.front(); Q.pop();
		
		if(D[here.y][here.x] <= here.cost) continue;
		
		D[here.y][here.x] = here.cost; 
		
		for(int d = 0; d < 4; d++) {
			ll ny = here.y + dy[d];
			ll nx = here.x + dx[d];
			
			if(ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
			if(ar[ny][nx] == '0') continue;
			
			Q.push({ny, nx, here.cost + 1 });
		}
	}
	cout << D[N-1][M-1];
}