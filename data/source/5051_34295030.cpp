#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define all(v) (v).begin(),(v).end()

using namespace std;
typedef long long ll;
typedef vector <ll> llv1;
typedef complex<double> base;

void fft(vector <base> &a, bool invert, bool integer_result=false) {
  int n = sz(a);
  for (int i=1,j=0;i<n;i++){
      int bit = n >> 1;
      for (;j>=bit;bit>>=1) j -= bit;
      j += bit;
      if (i < j) swap(a[i],a[j]);
  }
  for (int len=2;len<=n;len<<=1){
    double ang = 2*M_PI/len*(invert?-1:1);
    base wlen(cos(ang),sin(ang));
    for (int i=0;i<n;i+=len){
      base w(1);
      for (int j=0;j<len/2;j++){
        base u = a[i+j], v = a[i+j+len/2]*w;
        a[i+j] = u+v;
        a[i+j+len/2] = u-v;
        w *= wlen;
      }
    }
  }
  if (invert){
    for (int i=0;i<n;i++) {
      a[i] /= n;
      if(integer_result) {
        a[i] = base(round(a[i].real()), round(a[i].imag()));
      }
    }
  }
}
 
llv1 multiply(const llv1 &a,const llv1 &b) {
  vector <base> fa(all(a)), fb(all(b));
  int n = 1;
  while (n <= max(sz(a), sz(b))) n <<= 1;
  fa.resize(n); fb.resize(n);
  fft(fa,0,1); fft(fb,0,1);
  for (int i=0;i<n;i++) fa[i] *= fb[i];
  fft(fa,1,1);

  llv1 ret(n);
  for (int i=0;i<n;i++) {
    ret[i] = round(fa[i].real());
    // if(ret[i]) ret[i] = 1;
  };
  return ret;
}

llv1 cnt(2200000);
llv1 cnt2(550000);

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  ll N;

  cin >> N;
  cnt.resize(2*N);
  cnt2.resize(N);
  
  for(ll i = 1; i < N; i++) {
    cnt[(i*i)%N]++;
    cnt[((i*i)%N)+N]++;
    cnt2[(i*i)%N]++;
  }

  llv1 ret = multiply(cnt, cnt2);

  ll ans = 0;

  for1(0, N) {
    ans += cnt[i] * ret[i+N];
    ans += cnt[i] * cnt[2*i%N]; // 두 변이 같은 경우를 한번 더 더해줌.
  }
  cout << ans / 2;
}