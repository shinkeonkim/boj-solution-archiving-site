#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define INF (1ll << 60ll)

typedef long long ll;
typedef pair<ll, ll> pll;

ll N;

ll cnt;
ll command_cnt;

pll crt;
vector<string> board;

vector<vector<ll>> places; // y 좌표마다 x좌표를 박는다
vector<ll> mn;
vector<ll> mx;

ll min_y = INF;
ll min_x = INF;
ll max_y = -1;

vector <string> buffer;

void push(string dir, int idx) {
    command_cnt++;

    buffer.push_back(dir + " " + to_string(idx + 1) + " push\n");
    // cout << dir << " " << idx + 1 << " push\n";
}

void pull(string dir, int idx) {
    command_cnt++;
    // cout << dir << " " << idx + 1 << " pull\n";

    
    buffer.push_back(dir + " " + to_string(idx + 1) + " pull\n");
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    mn.resize(N, INF);
    mx.resize(N, -1);
    board.resize(N);
    places.resize(N);


    cin >> crt.fi >> crt.se;

    // 0-index

    crt.fi -= 1;
    crt.se -= 1;

    min_y = min(min_y, crt.fi);
    max_y = max(max_y, crt.fi);
    min_x = min(min_x, crt.se);


    for(int i = 0; i < N; i++) cin >> board[i];

    for(ll i = 0; i < N; i++) {
        for(ll j = 0; j < N; j++) {
            if(board[i][j] == '#') {
                cnt++;
                places[i].push_back(j);

                mn[i] = min(mn[i], j);
                mx[i] = max(mx[i], j);

                min_x = min(min_x, j);
                min_y = min(min_y, i);
                max_y = max(max_y, i);

            }
        }
    }

    for(ll i = 0; i < N; i++) {
        sort(places[i].begin(), places[i].end());
    }

    if(cnt == 0) {
        cout << "1\n";
        
        cout << "L " + to_string(crt.fi + 1) + " pull\n";
        return 0;
    }

    pll min_spot = {min_y, min_x};

    while(crt.se > min_spot.se) {
        // 원래 지점에서 왼쪽에서 오른쪽으로 쭉 쌓아넣는다.

        push("L", crt.fi);
        pull("R", crt.fi);
        
        crt.se -= 1;
    }

    for(int i = min_y; i < crt.fi; i++) {
        push("U", min_x);
    }

    for(int i = crt.fi + 1; i < max_y + 1; i++) {
        push("D", min_x);
    }


    for(int y = min_y; y <= max_y; y++) {
        for(int k = 0; k < mx[y] - min_x; k++) push("R", y);

        // cout << y << " " << places[y].size() << "**\n";
        if(places[y].size() == 0) {
            pull("L", y);
        }

        ll prev = min_x - 1;

        for(ll here : places[y]) {
            for(int k = prev + 1; k < here; k++) {
                if(k == min_x) {
                    pull("L", y);
                } else {
                    pull("D", k);
                }
            }

            prev = here;
        }
    }

    cout << command_cnt << "\n";
    for(int i = 0; i < command_cnt; i++) {
        cout << buffer[i];
    }
}