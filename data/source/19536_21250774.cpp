#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

long long N, Q;
vector<long long> cache, p_cache;
string str;
bool solve()
{
	long long r_pos = -1;
	for (int i = N - 1; i >= 0; i--)
	{
		if (str[i] == 'R') {
			r_pos = i;
			break;
		}
	}
	if (r_pos == -1)
		return false;

	long long r_sum = 0, right = 0;
	for (int i = N - 1; i >= 0; i--)
	{
		if (str[i] == 'R')
			break;
		if (str[i] == 'P') {
			r_sum += i - r_pos;
			right++;
		}
	}

	long long l_sum = 0;
	queue<long long> qq;
	for (int i = r_pos + 1; i < N; i++)
	{
		if (str[i] == 'P') {
			long long temp = i - r_pos;
			qq.push(temp);
			r_sum -= temp;
			l_sum += temp;
			right--;
			while (qq.size() > right)
			{
				l_sum -= qq.front();
				qq.pop();
			}
		}
		else {
			cache[i] = 2 * (r_sum - l_sum) + N - i;
			p_cache[i] = right + qq.size();
		}
	}
	return true;
}

void solve_left()
{
	long long r_pos = -1;
	for (int i = 0; i < N; i++)
	{
		if (str[i] == 'R') {
			r_pos = i;
			break;
		}
	}
	if (r_pos == -1)
		return;

	long long l_sum = 0, left = 0;
	for (int i = 0; i < N; i++)
	{
		if (str[i] == 'R')
			break;
		if (str[i] == 'P') {
			l_sum += r_pos - i;
			left++;
		}
	}

	long long r_sum = 0;
	queue<long long> qq;
	for (int i = r_pos - 1; i >= 0; i--)
	{
		if (str[i] == 'P') {
			long long temp = r_pos - i;
			qq.push(temp);
			l_sum -= temp;
			r_sum += temp;
			left--;
			while (qq.size() > left + 1)
			{
				r_sum -= qq.front();
				qq.pop();
			}
		}
		else {
			cache[i] = 2 * (l_sum - r_sum) + (r_pos + r_pos - i + 1);
			p_cache[i] = left + qq.size();
		}
	}
}

void solve_no()
{
	long long r_sum = 0, left = 0, right = 0;
	vector<long long> l_sum(1, 0);
	queue<long long> r_q;

	for (int i = N - 1; i >= 0; i--)
		if (str[i] == 'P')
			l_sum.push_back(l_sum.back() + N - i);
	left = l_sum.size() - 1;
	for (int i = N - 1; i >= 0; i--)
	{
		if (str[i] == 'P') {
			right++;
			left--;
			long long temp = N - i;
			r_sum += temp;
			r_q.push(temp);
			while (r_q.size() > left + 1)
			{
				r_sum -= r_q.front();
				r_q.pop();
			}
		}
		else {
			if (left >= right) {
				cache[i] = 2 * (l_sum[min(right * 2, (long long)l_sum.size() - 1)]
					- 2 * l_sum[right]) + N - i;
				p_cache[i] = right * 2;
			}
			else {
				cache[i] = 2 * (l_sum[l_sum.size() - 1] - l_sum[l_sum.size() - 1 - left] - r_sum)
					+ (2 * N - i + 1ll);
				p_cache[i] = left * 2 + 1;
			}
		}
	}
}

void solve_r()
{
	int last = -1, cnt = 0;
	for (int i = 0; i < N; i++)
	{
		if (str[i] == 'P')
			cnt++;
		if (str[i] == 'R') {
			if (last == -1) {
				cnt = 0;
				last = i;
			}
			else {
				for (int j = last + 1; j < i; j++)
					p_cache[j] = cnt;
				cnt = 0;
				last = i;
			}
		}
	}
}

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> Q;
	cache = vector<long long>(N, -1);
	p_cache = vector<long long>(N, 0);
	cin >> str;
	if(!solve())
		solve_no();
	else {
		solve_left();
		solve_r();
	}
	for (int i = 0; i < Q; i++)
	{
		int number;
		cin >> number;
		cout << p_cache[number - 1] << " " << cache[number - 1] << "\n";
	}
}