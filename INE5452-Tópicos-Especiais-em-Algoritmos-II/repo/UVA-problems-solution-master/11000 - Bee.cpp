#include <bits/stdc++.h>
using namespace std;
main()
{
    //freopen("txt.txt","r",stdin);
    long long int a,b,c,i,n,d,e;
    while(cin>>n , n>=0)
    {
        a=0,b=1,d=1;
        for (i = 1; i <= n; i++)
        {
            c = a + b;
            a = b;
            b = c;
            d=d+c;
        }

        cout<<d-b<<" "<<d<<endl;

    }

}


