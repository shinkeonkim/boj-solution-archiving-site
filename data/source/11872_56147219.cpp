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

int nim(int a) {
	if(a == 0) return 0;
		
	if(a % 4 == 0) return a - 1;
	if(a % 4 == 3) return a + 1;
	return a;
}


int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	// vector<int> nim(3000001);
	
	// nim[0] = 0;
	
	// for(int i = 1; i <= 300; i++) {
	// 	vector<int> chk(55);
		
	// 	for(int j = 0; j < i; j++) {
	// 		chk[nim[j]] = true;
	// 	}
		
	// 	for(int j = 1; j < i; j++) {
	// 		chk[nim[j] ^ nim[i - j]] = true;
	// 	}
		
			
	// 	for(int j = 0;; j++) {
	// 		if(!chk[j]) {
	// 			nim[i] = j;
	// 			break;
	// 		}
	// 	}
	// }
	
	// for1(0, 100) {
	// 	cout << nim[i] << " ";
	// }

	int n;
	
	cin >> n;
	
	int a, b;
	
	cin >> a;
	
	a = nim(a);
	
	for1(1, n) {
		cin >> b;
		a ^= nim(b);
	}

	cout << (a == 0 ? "cubelover" : "koosaga");
}