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

ll T, N;
bool D[1100000];

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	D[0] = 0;
	
	for1(1, 1000001) {
		bool chk = false;
		for(int j = 1; j * j <= i; j++) {
			if(D[i - j * j] == 0) {
				chk = true;
				break;
			}
		}
		D[i] = chk;
	}
	
	cin >> T;
	while(T--) {
		cin >> N;
		
		cout << (D[N] ? "koosaga" : "cubelover") << "\n";
	}
}