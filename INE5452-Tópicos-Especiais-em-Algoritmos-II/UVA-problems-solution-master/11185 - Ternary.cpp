#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    //freopen("txt.txt","r",stdin);
    ll int a,b,c,d,e[100],i,j;
    while(cin>>a)
    {
        c=0;
        if(a<0)
        {
            break;
        }
        if(a==0)
            cout<<0<<endl;
        else
        {
            while(a!=0)
            {
                b=a%3;
                e[c]=b;
                a/=3;
                c++;
            }

            for(j=c-1; j>=0; j--)
            {
                cout<<e[j];
            }
            cout<<endl;
        }

    }

}
