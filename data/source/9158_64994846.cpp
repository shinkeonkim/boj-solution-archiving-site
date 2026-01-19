#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

int n;
double x[105], y[105], z[105], X, Y, Z, d, e;

double dist(double a, double b, double c) {
	return a*a + b*b + c*c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cout << fixed;
    cout.precision(10);

    while(1) {
        cin >> n;

        if(n == 0) break;
        for (int i = 0; i < n; i++) {
            cin >> x[i] >> y[i] >> z[i];
            X += x[i];
            Y += y[i];
            Z += z[i];
        }

        X /= n; Y /= n; Z /= n;

        double P = 0.1;

        for (int i = 0; i < 70000; i++) {
            int f = 0;
            d = dist(X - x[0], Y - y[0], Z - z[0]);

            for (int j = 1; j < n; j++) {
                e = dist(X - x[j], Y - y[j], Z - z[j]);

                if (d < e) {
                    d = e;
                    f = j;
                }
            }
            X += (x[f] - X) * P;
            Y += (y[f] - Y) * P;
            Z += (z[f] - Z) * P;
            P *= 0.998;
        }

        d = dist(X - x[0], Y - y[0], Z - z[0]);
        
        for (int j = 1; j < n; j++) {
            e = dist(X - x[j], Y - y[j], Z - z[j]);

            if (d < e) {
                d = e;
            }
        }

        cout << sqrt(d) << "\n";
    }

    // cout << X << " " << Y << " " << Z << "\n";
}