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

int D[550][550];

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int N, M, a, b, c;
	
	cin >> N >> M;
	
	for1(0, N) {
		for1j(0, N) cin >> D[i][j];
	}
	
	for1(0, N) {
		for1j(0, N) {
			for(int k = 0; k < N; k++) {
				if(D[j][k] > D[j][i] + D[i][k]) D[j][k] = D[j][i] + D[i][k]; 
			}
		}
	}
	
	for1(0, M) {
		cin >> a >> b >> c;
		
		if(D[a-1][b-1] > c) cout << "Stay here";
		else cout << "Enjoy other party";
		cout << "\n";
	} 
	
}