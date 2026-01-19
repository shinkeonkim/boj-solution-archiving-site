#include <iostream>
#include <algorithm>
#define Mx 123456789
using namespace std;
int N;
int D[1100][5][5];
int ar[1100][5];
int main() {
    cin >> N;
    for(int y = 0; y < N; y++) {
        for(int x = 0; x<3; x++) cin >> ar[y][x];
    }

    for(int y=0; y<N;y++) {
        for(int x=0; x<3; x++) {
            for(int z =0; z<3; z++) D[y][x][z] = Mx;
        }
    }
    for(int x=0; x<3; x++) {
        D[0][x][x] = ar[0][x];
    }

    for(int y=1; y<N; y++) {
        for(int x1 = 0; x1 < 3; x1++) {
            for(int start = 0; start < 3; start++) {
                if(y == N-1) {
                    if(x1 != start) {
                        D[y][x1][start] = min(D[y-1][(x1+1)%3][start] , D[y-1][(x1+2)%3][start]) + ar[y][x1];
                    }
                }
                else {
                    D[y][x1][start] = min(D[y-1][(x1+1)%3][start] , D[y-1][(x1+2)%3][start]) + ar[y][x1];
                }


            }
        }
    }
    int ans = Mx;
    for(int x1 = 0; x1 < 3; x1 ++) {
        for(int start = 0; start < 3; start++) {
            ans = min(ans,D[N-1][x1][start]);
        }
    }
    cout<<ans;

}