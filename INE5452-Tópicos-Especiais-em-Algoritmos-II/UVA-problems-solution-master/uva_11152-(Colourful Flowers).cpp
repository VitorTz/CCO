#include<bits/stdc++.h>
#define PI 3.1415926535897
using namespace std;
int main()
{
    double a,b,c;
    double p,At,Ac,AC,r,ac,AT;
    while(cin>>a>>b>>c)
    {
        AC = 0,Ac=0,AT=0;
        r = c/2;
        p = ((a+b+c)/2);
        At = sqrt(p*(p-a)*(p-b)*(p-c));

        ac = (a*b*c)/(4*At);
        AC = ac*ac*PI-At;

        Ac = At - (PI*pow((At/p),2)) ;
        AT = At-Ac;
        printf("%.4f %.4f %.4f\n",AC,Ac,AT);


    }



}
