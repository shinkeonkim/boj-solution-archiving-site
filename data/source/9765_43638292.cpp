#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define MX 20000000

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll c[11], x[11];

bool d[22000000];
llv1 primes;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  for1(1, 7) {
    cin >> c[i];
  }

  fill(d+2, d+MX+1, true);

  for(int i = 2; i <= MX; i++) {
    if(d[i]) {
      primes.push_back(i);

      for(int j = i + i; j <= MX; j += i) {
        d[j] = false;
      }
    }
  }


  for(auto i : primes) {
    if(c[1] % i == 0 && c[5] % i == 0) {
      x[2] = i;
      x[1] = c[1] / i;
      x[3] = c[5] / i;
    }
    if(c[3] % i == 0 && c[6] % i == 0) {
      x[5] = i;
      x[6] = c[3] / i;
      x[4] = c[6] / i;
    }
  }

  for1(1, 7) {
    cout << x[i] << " ";
  }
}