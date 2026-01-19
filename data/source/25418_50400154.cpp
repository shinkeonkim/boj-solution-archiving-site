/*
  [25418: 정수 a를 k로 만들기](https://www.acmicpc.net/problem/25418)

  Tier: ??
  Category: DP, BFS
*/
#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define INF (ll)1e18

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll A, B;
ll D[4400000];
queue <pair <int, int>> Q;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  fill(D, D+4000001, INF);

  cin >> A >> B;

  Q.push({ A, 0 });

  while(!Q.empty()) {
    pair<int, int> f = Q.front();
    Q.pop();

    if(D[f.first] <= f.second) continue;

    D[f.first] = f.second;

    if(f.first + 1 <= B) {
      Q.push({ f.first + 1,  f.second + 1});
    }
    if(f.first * 2 <= B) {
      Q.push({ f.first * 2,  f.second + 1});
    }
  }

  cout << D[B];
}