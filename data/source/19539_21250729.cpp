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

ll N, S;
ll a;
ll cnt; // 1 카운트 하기
llv1 V;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;
    for1(0, N) {
        cin >> a;
        if(a == 0) continue;
        
        S += a;
        if(a == 1) cnt++;
        else {
            V.pb(a);
        }
    }

    if(S % 3 != 0) {
        cout << "NO";
        return 0;
    }

    sort(V.begin(), V.end());

    while(cnt > 0 && V.size() > 0) {
        cnt--;
        V[0]-=2;
        if(V[0] == 0) {
            V.erase(V.begin());
        } 
        else if(V[0] == 1) {
            cnt++;
            V.erase(V.begin());
        }
    }

    if(cnt > 0) {
        cout << "NO";
        return 0;
    }
    else {
        cout << "YES";
        return 0;
    }
}