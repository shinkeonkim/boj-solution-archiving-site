#include<iostream>
#include<algorithm>
#include<stack>
using namespace std;
int num[314]; // 전역변수로 선언하면 알아서 배열을 0으로 초기화함.
int n, d, inx, iny; // 전역변수로 선언하면 알아서 0으로 초기화함.
int row;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0}; // 방향 배열에 대한 명시를 조금더 편하게 하기!

struct st {
	int y;
	int x; // dir은 필요없는 정보인 것 같아요!
};

int main(){
	stack<st> stk; // C++ 구조체라는 걸 활용해보시는건 어떨까요?
	cin >> row; // >> 연산자 사이에는 공백을 넣어보기
	// char arr[55][55]; // 동적할당을 하지 않고 그냥 문자열 배열을 미리 선언하는게 정신건강에 좋아요. ㅋㅋㅋ
	string arr[55]; // 그리고 C++을 쓴다면 string을 활용해보는것도 더 좋을 것 같아요!
	int x,y;

	for(int i = 0; i < row; i++) cin >> arr[i];

	for(int i = 0; i < row; i++){
		for(int j = 0; j< row; j++){
			if(arr[i][j] != '1') continue;

			arr[i][j]='x';
			num[n]++;
			stk.push({i, j});

			while(!(stk.empty())){
				st t = stk.top();
				stk.pop();
				y = t.y;
				x = t.x;
				
				for(int d=0; d<4; d++){
					
					// 아래 조건은 너무 생각하기가 힘들것 같아요. 이런건 어떨까요?
					int next_y = y + dx[d];
					int next_x = x + dy[d];
					if(next_x < 0 || next_y < 0 || next_x >= row || next_y >= row || arr[next_y][next_x] !='1') continue;
					
					// if((d==0)&&(y==row-1)) continue;
					// else if((d==1)&&(y==0)) continue;
					// else if((d==2)&&(x==row-1)) continue;
					// else if((d==3)&&(x==0)) continue;
					num[n]++;
					arr[next_y][next_x]='x'; //이미 방이 포함되었다는 걸 x로
					stk.push({ next_y, next_x });
				}
			}
			n++;
		}
	}
	sort(num, num + n);
	cout << n << endl;
	for(int i = 0; i < n; i++) cout << num[i] <<endl;
	// for(int i=0;i<row;i++) delete[] arr[i];
	// delete[] arr; // 동적할당을 안했으니 메모리 해제도 필요없겠죠?
	return 0;
}