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

ll N, M, ans = 1;
string ar[55];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> M;
    for1(0, N) cin >> ar[i];

    for(ll d = 1; d<=min(N,M); d++) {
        for(ll y = 0; y <= N - d; y++) {
            for(ll x = 0; x <= M - d; x++) {
                if(ar[y][x] == ar[y+d][x] && ar[y+d][x] == ar[y][x+d] && ar[y][x+d] == ar[y+d][x+d]){
                    ans = max(ans, d + 1);
                }
            }
        }
    }
    cout << ans * ans;
}