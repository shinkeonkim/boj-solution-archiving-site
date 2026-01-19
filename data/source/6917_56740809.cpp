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

string s;
string A = "aeiou";

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	while(1) {
		cin >> s;
		if(s == "quit!") break;
		
		int n = s.length();
		if(n > 4 && s[n - 1] == 'r' && s[n - 2] == 'o' && A.find(s[n-3]) == string::npos) { 
			s[n - 1] = 'u';
			cout << s << "r\n";
			continue;
		}
		
		cout << s << "\n";
	}
}