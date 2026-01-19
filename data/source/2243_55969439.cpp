#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

const int MAX = 1100000;

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

// ll init(vector<ll>& a, vector<ll>& tree, ll node, ll start, ll end) {
// 	if(start == end) return tree[start] = a[start];
	
// 	tree[node] = init(a, tree, node * 2, start, (start + end) / 2) + 
// 		init(a, tree, node * 2 + 1, (start + end) / 2 + 1, end);
// }

void update(vector<ll>& tree, ll node, ll start, ll end, ll i, ll diff) {
	if(i < start || end < i) return;
	
	tree[node] += diff;
	
	if(start == end) return;
	
	update(tree, node * 2, start, (start + end) / 2, i, diff);
	update(tree, node * 2 + 1, (start + end) / 2 + 1, end, i, diff);
}

ll kth(vector<ll>& tree, ll node, ll start, ll end, ll k) {
	// idx 반환
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
	
	for1(0, n) {
		ll a, b, c;
		
		cin >> a >> b;
		
		if(a == 1) {
			ll idx = kth(tree, 1, 1, MAX, b);
			cout << idx << "\n";
			update(tree, 1, 1, MAX, idx, -1);
		} else {
			cin >> c;
			update(tree, 1, 1, MAX, b, c);
		}
	}	
}