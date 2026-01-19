#include <iostream>
#define Mx 999999999
using namespace std;
int V,E,a,b,c,ar[440][440]; 
int main() {
	cin>>V>>E;
	for(int x=1; x<=V; x++)
		for(int y=1; y<=V; y++) ar[x][y]=Mx;
	for(int x=0; x<E; x++) {
		cin>>a>>b>>c;
		ar[a][b]=c;
	}
	for(int z=1; z<=V; z++)
		for(int x=1; x<=V; x++)
			for(int y=1; y<=V; y++) {
				if(ar[x][y]>ar[x][z]+ar[z][y])
					ar[x][y]=ar[x][z]+ar[z][y];
			}
	int Min=Mx;
	for(int x=1; x<=V; x++) {
		if(Min>ar[x][x])Min=ar[x][x];
	}
	if(Min==Mx)cout<<-1;
	else cout<<Min;
}