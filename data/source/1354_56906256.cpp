#include <iostream>
#include <map>
#define MX 90000000
using namespace std;
typedef long long ll;

ll N, P, Q, X, Y;
map <ll, ll> m;

ll f(ll idx) {
  if(idx < 0) return 1;
  if(idx <= MX) {
    if(m[idx] == 0) {
      return m[idx] = f(idx/P - X) + f(idx/Q - Y);
    }
    else {
      return m[idx];
    }
  }
  
  return  f(idx/P - X) + f(idx/Q - Y);
  
}

int main() {
  cin >> N >> P >> Q >> X >> Y;

  m[0ll] = 1;
  cout << f(N);
}