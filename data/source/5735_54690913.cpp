#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int MAX_N = 4400;
const int MAX_CHAR = 330;

struct AhoCorasick {
	int trie[MAX_N][MAX_CHAR], piv;
	int fail[MAX_N]; // failure link
	int term[MAX_N]; // output check;
	
	void init(vector<string> &v) {
		// 초기화
		memset(trie, 0, sizeof(trie));
		memset(fail, 0, sizeof(fail));
		memset(term, 0, sizeof(term));
		
		piv = 0;
		
		for(auto &i : v) {
			int p = 0;
			for(auto &j : i) {
				if(!trie[p][j]) trie[p][j] = ++piv;
				p = trie[p][j];
			}
			term[p] = 1;
		}
		
		queue <int> que;
		
		for(int i = 0; i < MAX_CHAR; i++) {
			if(trie[0][i]) que.push(trie[0][i]);
		}
		
		while(!que.empty()) {
			int f = que.front();
			que.pop();
			
			for(int i = 0; i < MAX_CHAR; i++) {
				if(trie[f][i]) {
					int p = fail[f];
					while(p && !trie[p][i]) p = fail[p];
					p = trie[p][i];
					fail[trie[f][i]] = p;
					if(term[p]) term[trie[f][i]] = 1;
					que.push(trie[f][i]);
				}
			}
		}
	}
	
	bool query(string &s) {
		int p = 0;
		
		for(auto &i : s) {
			while(p && !trie[p][i]) p = fail[p];
			p = trie[p][i];
			if(term[p]) return 1;
		}
		return 0;
	}
	
	int count(string &s) {
		int p = 0;
		int ret = 0;
		
		for(auto &i : s) {
			while(p && !trie[p][i]) p = fail[p];
			p = trie[p][i];
			if(term[p]) {
				ret += 1;
				p = 0;
			}
		}
		
		return ret;
	}
} aho;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	while(1) {
		int N, Q;
		string s;
		vector<string> ar;

		cin >> N >> Q;
		cin.ignore();

		if(N == 0 && Q == 0) break;
		
		for(int i = 0; i < N; i++) {
			getline(cin, s);
			ar.push_back(s);
		}

		aho.init(ar);
		
		int ans = 0;

		for(int i = 0; i < Q; i++) {
			getline(cin, s);
			ans += aho.count(s);
		}
		
		cout << ans << "\n";
	}
}