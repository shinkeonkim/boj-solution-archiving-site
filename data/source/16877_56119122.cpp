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


int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int n;
	
	cin >> n;
	
	vector<int> fibos = {1, 1};
	vector<int> nim(3000001);
	
	for(int i = 2; i < 33; i++) {
		fibos.push_back(fibos[i - 1] + fibos[i-2]);
	}
	
	for(int i = 1; i <= 3000000; i++) {
		vector<int> chk(55);
		
		for(auto fibo : fibos) {
			if(i < fibo || fibo > 3000000) break;
			
			chk[nim[i - fibo]] = true;
		}
		
		for(int j = 0;; j++) {
			if(!chk[j]) {
				nim[i] = j;
				break;
			}
		}
	}
	
	int a, b;
	
	cin >> a;
	
	a = nim[a];
	
	for1(1, n) {
		cin >> b;
		a ^= nim[b];
	}

	cout << (a == 0 ? "cubelover" : "koosaga");
}