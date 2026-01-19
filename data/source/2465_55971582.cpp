#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

const int MAX = 110000;

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll init(vector<ll>& tree, ll node, ll start, ll end) {
	if(start == end) return tree[node] = 1;
	
	return tree[node] = init(tree, node * 2, start, (start + end) / 2) + init(tree, node * 2 + 1, (start + end) / 2 + 1, end);
}

void update(vector<ll>& tree, ll node, ll start, ll end, ll i, ll diff) {
	if(i < start || end < i) return;
	
	tree[node] += diff;
	
	if(start == end) return;
	
	update(tree, node * 2, start, (start + end) / 2, i, diff);
	update(tree, node * 2 + 1, (start + end) / 2 + 1, end, i, diff);
}

ll kth(vector<ll>& tree, ll node, ll start, ll end, ll k) {
	if(start == end) return start;
	
	if(k <= tree[node * 2]) return kth(tree, node * 2, start, (start + end) / 2, k);
	
	return kth(tree, node * 2 + 1, (start + end) / 2 + 1, end, k - tree[node * 2]);
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	vector <ll> tree(1 << (((int)ceil(log2(MAX + 1))) + 1));

	ll n;
	
	cin >> n;
	
	vector <ll> a(n);
	
	vector <ll> order(n);
	
	map<ll, ll> d;
	
	for1(0, n) {
		cin >> a[i];
	}
	
	sort(a.begin(), a.end());
	
	for1(0, n) {
		d[i + 1] = a[i];
	}
	
	for1(0, n) cin >> order[i];
	
	init(tree, 1, 1, n);
	
	vector<ll> ans(n + 1);
	
	for(int i = 0; i < n; i++) {
		int idx = n - i - 1;
		int f_idx = order[idx] + 1;
		
		ll k = kth(tree, 1, 1, n, f_idx);
		
		ans[idx] = d[k];
		update(tree, 1, 1, n, k, -1);
	}
	
	for1(0, n) {
		cout << ans[i] << "\n";
	}
}