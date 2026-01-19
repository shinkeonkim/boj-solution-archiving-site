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

ll N, M, K;
ll ar[1100][1100];
ll D[1100][1100];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    for1(0, N) {
        for1j(0, M) {
            cin >> ar[i][j];
        }
    }

    for1(0, N) {
        for1j(0, M) {
            if(i == 0 && j == 0) D[i][j] = ar[i][j];
            else if(i == 0) D[i][j] = D[i][j-1] + ar[i][j];
            else if(j == 0) D[i][j] = D[i-1][j] + ar[i][j];
            else D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + ar[i][j]; 
        }
    }

    cin >> K;
    while(K--) {
        ll x1, y1, x2, y2;
        cin >> y1 >> x1 >> y2 >> x2;
        x1--;y1--;x2--;y2--;
        ll ans = D[y2][x2];
        if(x1>0) ans -= D[y2][x1-1];
        if(y1>0) ans -= D[y1-1][x2];
        if(x1>0&&y1>0) ans += D[y1-1][x1-1];
        cout << ans << "\n";
    }
    
}