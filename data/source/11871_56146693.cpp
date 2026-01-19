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
	
	a -= 1;
	
	int b = a / 4 * 2;
	vector<int> c = {1, 0, 2, 1};
	
	return c[a % 4] + b;
	
}


int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int n;
	
	cin >> n;

	// vector<int> nim(3000001);
	
	// nim[0] = 0;
	// nim[1] = 1;
	// nim[2] = 0;
	
	// for(int i = 3; i <= 300; i++) {
	// 	vector<int> chk(55);
		
	// 	if(i % 2 == 1) {
	// 		for(int j = 2; j <= i; j+=2) {
	// 			chk[nim[i - j]] = true;
	// 		}
	// 		chk[nim[0]] = true;
	// 	} else {
	// 		for(int j = 2; j < i; j+=2) {
	// 			chk[nim[i - j]] = true;
	// 		}
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
	
	int a, b;
	
	cin >> a;
	
	a = nim(a);
	
	for1(1, n) {
		cin >> b;
		a ^= nim(b);
	}

	cout << (a == 0 ? "cubelover" : "koosaga");
}