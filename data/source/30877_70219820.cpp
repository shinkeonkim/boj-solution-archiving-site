#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int N;
  
    cin >> N;
  
    while (N --) {
        string a, b;
        cin >> a >> b;
        
        int idx = -1;
        for(int i = 0; i < a.length(); i++) {
            if(a[i] == 'x' or a[i] == 'X') {
                idx = i;
                break;
            } 
        }
        cout << (char) toupper(b[idx]);
    }
}