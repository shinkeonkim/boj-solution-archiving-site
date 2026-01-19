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
typedef vector <vector<int>> iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull>> ullv2;

ll a, b, c;
ll d, e, f;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> a >> b >> c;
    cin >> d >> e >> f;

    for(int x = -999; x <= 999; x++) {
        for(int y = -999; y <= 999; y++) {
            if(a * x + b * y == c && d * x + e * y == f) {
                cout << x << " " << y << " ";
                return 0;
            }
        }
    }
    
}