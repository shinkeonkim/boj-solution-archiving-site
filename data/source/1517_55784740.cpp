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

int l;

void update(vector<ll>& tree, int i, int diff) {
	while(i <= l) {
		tree[i] += diff;
		i += i & -i;
	}
}

ll sum(vector<ll>& tree, int i) {
	ll ans = 0;
	while(i > 0) {
		ans += tree[i];
		i -= i & -i;
	}
	return ans;
}

ll sum(vector<ll>& tree, int l, int r) {
	if(l > r) return 0;
	return sum(tree, r) - sum(tree, l - 1);
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	ll n, tmp;
	cin >> n;
	
	vector <ll> a(n);
	vector <ll> b(n);
	
	map<ll, ll> pos;
	
	for1(0, n) {
		cin >> a[i];
		b[i] = a[i];
	}
	
	sort(b.begin(), b.end());
	b.erase(unique(b.begin(), b.end()), b.end());
	
	map<ll, ll> d;
	for(int i = 0; i < b.size(); i++) {
		d[b[i]] = i + 1;
	}
	
	for1(0, n) {
		a[i] = d[a[i]];
	}
	
	ll ans = 0;
	
	vector<ll> tree(n + 1);
	
	l = n;
	
	for1(0, n) {
		ans += sum(tree, a[i] + 1, n);
		update(tree, a[i], 1);
	}
	
	cout << ans;	
}