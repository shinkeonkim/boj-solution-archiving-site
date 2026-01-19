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
typedef pair<int, int> pii;

int N;
int ar[1100000][5];

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	
	for1(0, N) {
		for1j(0, 5) cin >> ar[i][j];
	}
	
	int ans = 0;
	pii d = {0, 1};
	
	for1(0, 5) {
		for1j(i+1, 5) {
			int cnt = 0;
			
			for(int k = 0; k < N; k++) {
				if(ar[k][i] && ar[k][j]) cnt++;
			}
			
			if(ans < cnt) {
				ans = cnt;
				d = {i, j};
			}
		}
	}
	
	cout << ans << "\n";
	for1(0, 5){
		if(i == d.first || i == d.second) cout << "1 ";
		else cout << "0 ";
    }
}
