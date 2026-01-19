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
#include <bits/stdc++.h>
using namespace std;

ll uf[220000];

ll find(ll a){
    if(uf[a] < 0) return a;
    return uf[a] = find(uf[a]);
}

bool merge(ll a, ll b){
    a = find(a);
    b = find(b);
    if(a == b) return false;
    uf[b] = a;
    return true;
}

struct Edge{
    ll u, v, w;
    Edge(): Edge(-1, -1, 0){}
    Edge(ll u1, ll v1, ll w1): u(u1), v(v1), w(w1){}
    bool operator <(const Edge& O)const{ return w < O.w; }
};

ll N, M, a, b, c;
Edge e[220000];

int main(){
		ios::sync_with_stdio(0);
		cin.tie(0);
		cout.tie(0);
	
		while(1) {
				cin >> N >> M;

				ll result = 0, cnt = 0;
			
				if(N == M && M == 0) break;
				for(int i=0; i < M; i++){
						cin >> a >> b >> c;
						e[i] = Edge(a, b, c);
						result += c;
				}

				sort(e, e+M);

				fill(uf, uf+N, -1);
				for(int i=0; ; i++) {
						if(merge(e[i].u, e[i].v)) {
								result -= e[i].w;
								if(++cnt == N-1) break;
						}
				}
				cout << result << "\n";	
		}
}