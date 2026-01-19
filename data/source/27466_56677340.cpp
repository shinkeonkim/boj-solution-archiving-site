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

ll N, M;
string s, ans;
stack <char> stk;
string A = "AEIOU";

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N >> M >> s;
	
	int crt = 0;
	
	for(int i = N - 1; i > -1; i--) {
		if(crt == 0) {
			if(A.find(s[i]) != string::npos) {
				continue;
			}
			
			stk.push(s[i]);
			crt++;
		}	
		else if(crt == 1 || crt == 2) {
			if(s[i] != 'A') continue;
			
			stk.push(s[i]);
			crt++;
		} else {
			if(crt < M) {
				stk.push(s[i]);
				crt++;
			}
		}
	}
	
	if(stk.size() < M) cout << "NO";
	else {
		cout << "YES\n";
		
		while(!stk.empty()) {
			cout << stk.top();
			stk.pop();
		}
	}
	
}