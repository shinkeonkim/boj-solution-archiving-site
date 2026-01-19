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

ll N, ans;
string ar[55];

ll check() {
	ll ret = 0;
	ll crt;
	
	for(int i = 0; i < N; i++) {
		crt = 1;
		for(int j = 1; j < N; j++) {
			if(ar[i][j - 1] != ar[i][j]) {
				ret = max(ret, crt);
				crt = 1;
			} else {
				crt++;
			}
		}
		ret = max(ret, crt);	
	}
	
	
	for(int i = 0; i < N; i++) {
		crt = 1;
		
		for(int j = 1; j < N; j++) {
			if(ar[j-1][i] != ar[j][i]) {
				ret = max(ret, crt);
				crt = 1;
			} else {
				crt++;
			}
		}
		ret = max(ret, crt);
	}
	
	return ret;
}


int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	for1(0, N) {
		cin >> ar[i];
	}
	
	for(int i = 0; i < N; i++) {
		for(int j = 0; j < N; j++) {
			if(j + 1 < N) {
				char tmp;
				tmp = ar[i][j];
				ar[i][j] = ar[i][j+1];
				ar[i][j+1] = tmp;
				
				ans = max(ans, check());
		
				tmp = ar[i][j];
				ar[i][j] = ar[i][j+1];
				ar[i][j+1] = tmp;
			}
			
			if(i + 1 < N) {
				char tmp;
				tmp = ar[i][j];
				ar[i][j] = ar[i+1][j];
				ar[i+1][j] = tmp;
				
				ans = max(ans, check());

				tmp = ar[i][j];
				ar[i][j] = ar[i+1][j];
				ar[i+1][j] = tmp;
			}
		}
	}
	
	cout << ans;
}