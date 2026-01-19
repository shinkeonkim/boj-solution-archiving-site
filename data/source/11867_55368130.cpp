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

ll a, b;
bool chk[110][110];
bool d[110][110];

bool f(ll i, ll j) {
	if(i == 1 && j == 1) return 0;
	
	if(chk[i][j]) return d[i][j];
	
	if(i > j) swap(i, j);
	
	bool flag = false;
	for(int k = 1; k < i; k++) {
		bool ret = !f(k, i - k);
		
		if(ret) {
			flag = true;
			break;
		}
	}

	for(int k = 1; k < j; k++) {
		bool ret = !f(k, j - k);
		
		if(ret) {
			flag = true;
			break;
		}
	}
	
	d[i][j] = d[j][i] = flag;
    chk[i][j] = chk[j][i] = true;
    
    return d[i][j];
}


int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> a >> b;
	cout << (f(a, b) ? "A" : "B");
}