#import<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n,m,ans;
priority_queue <ll,vector<ll>,less<ll>> Q;
int main() {
    cin >> n;
    for(ll x=0; x<n; x++) {
        cin >> m;
        Q.push(m-x);
        if(!Q.empty() && Q.top() > m-x) { 
            ans += Q.top()-m + x;
            Q.pop();
            Q.push(m-x);
        }
    }
    cout<<ans;
}