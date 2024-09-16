#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long
#define pb push_back

ll int revers(ll int n)
{
    ll int k,r=0;
    while(n!=0)
    {
        k=n%10;
        r=r*10+k;
        n/=10;
    }
    return r;

}
int main()
{
//freopen("txt.txt","r",stdin);
    fast
    ll int t,a,b,c,d,e,n;
    cin>>t;
    while(t--)
    {
        n=1;
        cin>>a;
        while(1)
        {
            b=revers(a);
            a=a+b;
            c=revers(a);
            if(a==c)
            {
                break;
            }
            n++;
        }
        cout<<n<<" "<<c<<endl;
    }

}
