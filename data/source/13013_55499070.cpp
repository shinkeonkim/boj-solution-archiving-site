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

ll n;
ll ar[55];
ll place[55];

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> n;
	for1(0, n) {
		cin >> ar[i];
		place[ar[i]] = i;
	}
	
	place[n] = -1;
	
	int cnt = 1;
	
	for(int i = 0; i < n - 1; i++) {
		if(place[ar[i] + 1] > place[ar[i + 1] + 1]) cnt++;	
	}
	
	cout << cnt;
}