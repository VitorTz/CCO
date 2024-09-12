#include <bits/stdc++.h>
using namespace std;
main()
{
    //freopen("txt.txt","r",stdin);
    long long int c,d,t=1;
    while(cin>>c, c!=0)
    {
        d=ceil((3+sqrt(9+4*2*c))/2);
        cout<<"Case "<<t++<<": "<<d<<endl;
    }
}
