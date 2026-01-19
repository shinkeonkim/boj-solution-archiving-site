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

// int nim(int a) {
// 	if(a == 0) return 0;
		
// 	if(a % 4 == 0) return a - 1;
// 	if(a % 4 == 3) return a + 1;
// 	return a;
// }


int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	vector<int> nim(1001);
	
	for(int i = 1; i <= 1000; i++) {
		vector<int> chk(1001);
		
		for(int j = 2; j <= i; j++) {
			chk[nim[j - 2] ^ nim[i - j]] = true;
		}
					
		for(int j = 0;; j++) {
			if(!chk[j]) {
				nim[i] = j;
				break;
			}
		}
	}
	
	int n;
	
	cin >> n;
	
	cout << (nim[n] > 0 ? 1 : 2);
}