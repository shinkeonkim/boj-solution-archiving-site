#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define INF 9876543

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

struct st {
	int a, b, c;
};

bool comp(st a, st b) {
	return a.a < b.a;
}

void init(vector<int>& tree, int node, int start, int end) {
	tree[node] = INF;
	
	if(start == end) return;
	
	init(tree, node * 2, start, (start + end) / 2);
	init(tree, node * 2 + 1, (start + end) / 2 + 1, end);
}

void update(vector<int>& tree, int node, int start, int end, int i, int value) {
	if(i < start || end < i) return;
	
	tree[node] = min(tree[node], value);
	
	if(start == end) return;
	
	update(tree, node * 2, start, (start + end) / 2, i, value);
	update(tree, node * 2 + 1, (start + end) / 2 + 1, end, i, value);	
}

int minimum(vector<int>& tree, int node, int start, int end, int left, int right) {
	if(end < left || right < start) return INF;
	if(left <= start && end <= right) return tree[node];
	if(start == end) return tree[node];
	
	return min(minimum(tree, node * 2, start, (start + end) / 2, left, right), minimum(tree, node * 2 + 1, (start + end) / 2 + 1, end, left, right));
}

vector<int> tree(2200000);

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int N;

	cin >> N;
	
	vector <st> grades(N + 1);

	int a;
	
	for1(0, N) {
		cin >> a;
		grades[a].a = i + 1;
	}
	for1(0, N) {
		cin >> a;
		grades[a].b = i + 1;
	}
	for1(0, N) {
		cin >> a;
		grades[a].c = i + 1;
	}
	
	sort(grades.begin(), grades.end(), comp);
	
	init(tree, 1, 1, N);
	
	int cnt = 0;

	for1(1, N + 1) {
		int b = grades[i].b;
		int c = grades[i].c;
		
		int mn = minimum(tree, 1, 1, N, 1, b);
		
		if(mn > c) cnt++;
		
		update(tree, 1, 1, N, b, c);
	}
	
	cout << cnt;
}