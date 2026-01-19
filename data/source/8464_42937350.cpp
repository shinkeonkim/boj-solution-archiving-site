#include <iostream>
#include <vector>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

ll mo[3300000];

void mobius(ll mx) {
  for(ll x = 1; x <= mx; x++) {
    mo[x] = 1;
  }
  for(ll x = 2; x <= mx; x++) {
    if(mo[x] == 1) {
      for(ll y = x; y <= mx; y += x) {
        mo[y] *= -x;
      }
      for(ll y = x * x; y <= mx; y += x * x) {
        mo[y] = 0;
      }
    }
  }
  for(ll x = 2; x <= mx; x++) {
    if(mo[x] == x) mo[x] =1;
    else if(mo[x] == -x) mo[x] = -1;
    else if(mo[x] <0) mo[x] =1;
    else if(mo[x] >0) mo[x] =-1;
  }
}

ll free_count(ll K) {
  ll ret = 0;
  for(ll x = 1; x * x <= K; x++) {
    ret += mo[x] * (K / (x * x));
  }
  return ret;
}

int main() {
  ll K, S=1, E=50000000000ll, mid;
  ll answer = E;
  mobius(3000000);

  cin >> K;

  while(S<=E) {
    mid = (S+E)/2;
    if(mid - free_count(mid) >= K) {
      if(answer > mid) answer = mid;
      E = mid - 1;
    }
    else {
      S = mid + 1;
    }
  }
  cout<<answer;
}
