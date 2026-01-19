#include <iostream>
using namespace std;
int main() {
  int b[26]={0};
  char ch;
  do {
    cin.get(ch);
    if (ch>='a'&&ch<='z')b[ch-'a']++;
    if (ch>='A'&&ch<='Z')b[ch-'A']++;
  }
  while (ch !='@');

  int max=b[0];
  for (int i=1;i<26;i++)
    if (b[i]>max)max=b[i];

   while(max > 0) {
     for (int i = 0; i < 26;i++)
       if (max - b[i] <= 0) cout << char(i + 'A');
       else cout << " ";
     max--;
     cout<<endl;
   }
   for (char i=0; i<26; i++) cout<<"-";
   cout<<endl;
   for (char i='A';i<='Z';i++) cout<<i;
   cout<<endl;
 }