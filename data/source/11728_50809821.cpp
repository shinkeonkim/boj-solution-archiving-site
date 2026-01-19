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

int N, M;
int a, b;
int arr_a[1100000];
int arr_b[1100000];

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N >> M;

  vector <int> ans;

  for1(0, N) {
    cin >> arr_a[i];
  }

  for1(0, M) {
    cin >> arr_b[i];
  }

  while(a < N && b < M) {
    if(arr_a[a] < arr_b[b]) {
      ans.push_back(arr_a[a]);
      a++;
    } else {
      ans.push_back(arr_b[b]);
      b++;
    }
  }

  while(a < N) {
    ans.push_back(arr_a[a++]);
  }

  while(b < M) {
    ans.push_back(arr_b[b++]);
  }

  for(int i : ans) {
    cout << i << " ";
  }
}