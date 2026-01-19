/*
1 2
1 2

1 2 3
3 2 1

1 2 3 4
3 2 1 4

1 2 3 4 5
1 2 5 4 3

1 2 3 4 5 6
1 6 5 4 3 2

1 2 3 4 5 6 7
7 6 5 4 3 2 1

1 2 3 4 5 6 7 8
7 6 5 4 3 2 1 8

1 2 3 4 5 6 7 8 9
1 6 5 4 3 2 9 8 7
*/

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

int N;
int D[11000];

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  cin >> N;

  for(int i = N; i > 0; i--) {
    if(D[i]) continue;

    int z = 2;
    while(true) {
      if(z > i && !D[z-i]) {
        D[i] = z-i;
        D[z-i] = i;
        break;
      }
      z <<= 1;
    }
  } 

  for(int i = 1; i <= N; i++) {
    cout << D[i] << "\n";
  }
}