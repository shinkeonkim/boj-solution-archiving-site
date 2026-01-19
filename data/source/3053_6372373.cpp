#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>
using namespace std;
int R;
int main()
{
	scanf("%d",&R);
	printf("%.6lf\n%.6lf",(double)R*R*M_PI,(double)2*R*R);
}