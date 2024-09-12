#include <bits/stdc++.h>
using namespace std;
#define PI acos(-1)

int main()
{
    //freopen("txt.txt","r",stdin);
    double a,b,c,r;
    int t;
    cin>>t;
    while(t--)
    {
        cin>>a;
        c=a*0.6;
        b=a/5;
        r=PI*(b*b);
        cout<<fixed;
        cout<<setprecision(2)<<r<<" "<<(c*a)-r<<endl;

    }
}
