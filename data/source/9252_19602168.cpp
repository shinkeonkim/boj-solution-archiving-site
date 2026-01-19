#include <iostream>
#include <string>
using namespace std;

int check[1100][1100],Cnt[1100][1100];
string a,b;
char answer[2200];

int main() {
	cin>>a>>b;
	for(int y=0; y<a.length(); y++) {
		for(int x=0; x<b.length(); x++) {
			if(a[y]==b[x]) {
				Cnt[x+1][y+1]=Cnt[x][y]+1;
				check[x+1][y+1]=3; //대각선 3번 
			}
			else if(a[y]!=b[x]) {
				if(Cnt[x+1][y]<Cnt[x][y+1]) {
					check[x+1][y+1]=2; //왼쪽거 2번 
					Cnt[x+1][y+1]=Cnt[x][y+1];
					
				}
                else {
                    check[x+1][y+1]=1;
                    Cnt[x+1][y+1]=Cnt[x+1][y]; //위에거 1번 
                } 
			}
		}
	}
	
	int X=b.length(); int Y=a.length();
	int Cnt1=0;
	
	while(X>0&&Y>0) {
		if(check[X][Y]==3) {
			answer[Cnt1]=b[X-1];
			X-=1; Y-=1;
			Cnt1++;
		}
		else if(check[X][Y]==2) {
			X--;
		}
		else if(check[X][Y]==1) {
			Y--;
		}
        else {
            break;
        }
	}
	cout<<Cnt[b.length()][a.length()]<<endl;
	for(int x=Cnt[b.length()][a.length()]-1; x>=0; x--) cout<<answer[x];
}