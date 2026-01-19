#include <iostream>
#include <string>
using namespace std;

string s;
int k;
bool answer = true;

int main() 
{
    cin >> s;
    if(s.length() != 1)
    {
        k = s[1] - s[0];
        for(int i = 1; i < s.length()-1; i ++) {
            if(k != s[i+1]-s[i]) {
                answer = false;
            }
        }
    }
    
    if(answer) {
        cout << "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!";
    }
    else {
        cout << "흥칫뿡!! <(￣ ﹌ ￣)>";
    }
}