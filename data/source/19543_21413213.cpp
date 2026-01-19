#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <queue>
#include <stack>

typedef long long ll;

using namespace std;

int N, M, K;
vector<string> blocks;
string block_str;
vector<vector<pair<int, int>>> vec;

void init()
{
	vec.resize(K);
	for (int i = 0; i < K; i++)
	{
		ll sum = 0, last = -1;
		for (int j = 0; j < M; j++)
		{
			if (blocks[i][j] == 'R') {
				sum++;
				if (last == -1)
					last = j;
			}
			if (blocks[i][j] == 'U') {
				if (last == -1)
					last = j;
				vec[i].push_back(make_pair(j, last));
				sum = 0;
				last = -1;
			}
		}
	}
}

ll solve(int l, int r, int idx)
{
	if (idx == -1)
		return 0;

	int current = block_str[idx] - 'A';
	int _ll = lower_bound(vec[current].begin(), vec[current].end(), make_pair(l, 0)) - vec[current].begin();
	if (_ll == vec[current].size())
		return 0;
	auto it_r = lower_bound(vec[current].begin(), vec[current].end(), make_pair(r, 0));
	int rr = it_r - vec[current].begin();
	if (rr >= vec[current].size() || vec[current][rr].first > r) {
		if (rr == 0)
			return 0;
		rr = (it_r - 1) - vec[current].begin();
	}

	ll next_l = vec[current][_ll].second;
	ll next_r = vec[current][rr].first;
	return next_r - next_l + 1ll + solve(next_l, next_r, idx - 1);
}

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M >> K;
	blocks.resize(K);
	for (int i = 0; i < K; i++)
		cin >> blocks[i];
	cin >> block_str;
	init();

	int current = block_str[block_str.size() - 1] - 'A';
	int l = 0;
	for (int i = M - 2; i >= 0; i--)
	{
		if (blocks[current][i] == 'U') {
			l = i + 1;
			break;
		}
	}

	cout << solve(l, M - 1, block_str.size() - 2) + M - l << endl;
}