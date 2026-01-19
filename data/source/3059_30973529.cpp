#include <iostream>
#include <cstring>
using namespace std;
int main() {
	int loop;
	cin >> loop;
	for (int a = 0; a < loop; a++) {
	int num[26];
	for (int i = 0; i < 26; i++) {
		num[i] = 65 + i;
	}
	char arr[1100];
	cin >> arr;
	int len = strlen(arr);
	for (int i = 0; i < len; i++) {
		for (int j = 0; j < 26; j++) {
			if (arr[i] == num[j]) {
				num[j] = 0;
			}
		}
	}
	int sum = 0;
	for (int i = 0; i < 26; i++) {
		sum = sum + num[i];
	}
	cout << sum << endl;
	}
}