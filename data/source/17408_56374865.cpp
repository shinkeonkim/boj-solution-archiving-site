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

const int MAX = 200000;

ll N;
ll ar[110000];

void init(vector<ll>& tree, ll node, ll s, ll e) {
	if(s == e) {
		tree[node] = s;
		return;
	}
	int mid = (s + e) / 2;
	
	init(tree, node * 2, s, mid);
	init(tree, node * 2 + 1, mid + 1, e);
	
	if(ar[tree[node * 2]] > ar[tree[node * 2 + 1]]) {
		tree[node] = tree[node * 2];
	} else {
		tree[node] = tree[node * 2 + 1];	
	}
}

void update(vector<ll>& tree, ll node, ll s, ll e, ll i, ll val) {
	if(i < s || e < i) return;
	
	if(s == e) {
		ar[i] = val;
		tree[node] = s;
		return;
	}
	
	int mid = (s + e) / 2;
	
	update(tree, node * 2, s, mid, i, val);
	update(tree, node * 2 + 1, mid + 1, e, i, val);
	
	if(ar[tree[node * 2]] > ar[tree[node * 2 + 1]]) {
		tree[node] = tree[node * 2];
	} else {
		tree[node] = tree[node * 2 + 1];
	}
}

ll maximum(vector<ll>& tree, ll node, ll s, ll e, ll l, ll r) {
	if(l > e || r < s) return 0;
	if(l <= s && e <= r) return tree[node];
	
	int mid = (s + e) / 2;
	
	ll left = maximum(tree, node * 2, s, mid, l, r);
	ll right = maximum(tree, node * 2 + 1, mid + 1, e, l, r);
	
	if(ar[left] < ar[right]) return right;
	return left;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	for1(1, N + 1) cin >> ar[i];
	
	int h = (int)ceil(log2(MAX));
	int tree_size = (1 << (h + 1));
	vector<ll> tree(tree_size);
	
	init(tree, 1, 0, N);
	
	ll M, a, b, c;
	
	cin >> M;
	
	while(M--) {
		cin >> a >> b >> c;
		
		if(a == 1) {
			ar[b] = c;
			update(tree, 1, 0, N, b, c);
		} else {
			ll mx = maximum(tree, 1, 0, N, b, c);
			ll ans = ar[mx];
			
			if(mx - 1 >= b) {
				ll mx1 = maximum(tree, 1, 0, N, b, mx - 1);
				ans = max(ans, ar[mx] + ar[mx1]);
			}
			
			if(mx + 1 <= c) {
				ll mx2 = maximum(tree, 1, 0, N, mx + 1, c);
				ans = max(ans, ar[mx] + ar[mx2]);			
			}

			cout << ans << "\n";
		}
	}
}