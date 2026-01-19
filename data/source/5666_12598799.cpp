#include <cstdio>
using namespace std;
double A,B;
int main()
{
    while(scanf("%lf %lf",&A,&B)!=EOF)
    {
        printf("%.2lf\n",A/B);
    }
}