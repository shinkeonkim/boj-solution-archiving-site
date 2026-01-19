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

ll N, jj_cnt, dd_cnt, a, b;
llv1 edge[330000];
bool check[330000];


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;
    for1(0, N-1) {
        cin >> a >> b;
        edge[a].pb(b);
        edge[b].pb(a);
    }

    for1(1,N+1) {
        ull k = edge[i].size();
        if(k<3) continue;
        jj_cnt += (k*(k-1ll)/2ll)*(k-2ll)/3ll;
    }

    for1(1, N+1) {
        check[i] = true;
        ll s = edge[i].size();
        for(auto j : edge[i]) {
            if(!check[j]) {
                ll second_node = j;
                dd_cnt += (s-1) * (edge[second_node].size() - 1);
                // cout << i << " " << j << " " << (s-1) * (edge[second_node].size() - 1) << "\n";
            }
        }
    }

    // cout <<"\n" <<dd_cnt << " " << jj_cnt;

    if(dd_cnt == jj_cnt *3) {
        cout << "DUDUDUNGA";
    }
    else if(dd_cnt < jj_cnt * 3) {
        cout << "G";
    }
    else {
        cout << "D";
    }
}