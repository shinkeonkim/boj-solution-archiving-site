#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll tc;
ll N;
string s;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> tc;
	
	for(int t = 1; t <= tc; t++) {
		cin >> N;
		cin >> s;
		
		int crt = 0;
		
		cout << "Case #" << t << ": ";
		
		cout << ++crt << " ";
		
		for(int i = 1; i < N; i++) {
			if(s[i - 1] >= s[i]) {
				crt = 0;
			}
			cout << ++ crt << " ";
		}
		
		cout << "\n";
	}
}