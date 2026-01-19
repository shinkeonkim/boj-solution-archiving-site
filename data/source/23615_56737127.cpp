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

ll N;
ll ar[110000];
ll z_count;

bool comp(ll a, ll b) {
	if(a < 0) a *= -1;
	if(b < 0) b *= -1;
	
	return a < b;
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	for1(0, N) {
		cin >> ar[i];
		
		if(ar[i] == 0) z_count++;
	}
	
	if(z_count > 0) {
		if(z_count >= 2) {
			cout << "Yes\n0";
			return 0;
		} else {
			cout << "No";
			return 0;
		}
	}
	
	sort(ar, ar+N, comp);
	
	ll d = ar[N - 1];
	
	bool flag = true;
	for1(0, N - 1) {
		if(d % ar[i] > 0) {
			flag = false;
		}
		
		d /= ar[i];
	}
	
	if(flag && d == 1) {
		cout << "Yes\n" << ar[N - 1];
	} else {
		cout << "No";
	}
}