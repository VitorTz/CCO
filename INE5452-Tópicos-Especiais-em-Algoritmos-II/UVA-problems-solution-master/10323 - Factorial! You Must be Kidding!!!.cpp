#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long

int main()
{
//freopen("txt.txt","r",stdin);
    fast
    ll int t,a,b,c,d,e,n;
    while(cin>>b)
    {
        a=1;
        if(b>=8 && b<=13)
        {
            b=abs(b);
            for(int i=1;i<=b;i++)
            {
                a*=i;
            }
            cout<<a<<endl;

        }
        else if(b>13 || (b<0 && b%2!=0))
        {
            cout<<"Overflow!"<<endl;
        }
        else
        {
            cout<<"Underflow!"<<endl;
        }

    }
}
