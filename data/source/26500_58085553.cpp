#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int tc;
    cin >> tc;
    while (tc--) {
        double a, b;
        
        cin >> a >> b;

        if (b > a) {
            double temp = a;
            a = b;
            b = temp;
        }

        double res = a - b;
        printf("%.1lf\n", res);
    }

    return 0;
}
