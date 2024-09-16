#include<bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long
#define pb push_back

bool prime[1000001];
void sieve( int n )
{
    int x = sqrt( n );
    prime[0] = 1;
    prime[1] = 0;
    for( int i = 4; i <= n; i += 2 )
        prime[i] = 1;
    for( int i = 3; i <= x; i += 2 )
    {
        if( prime[i] == 0 )
        {
            for( int j = i+i; j <= n; j += i )
                prime[j] = 1;
        }
    }
    return;
}
int main()
{
    //freopen("input.txt","r",stdin);
    fast
    sieve(100000);
    ll int a,b,c,d,n,t,p,q,r,count,cs,mn;

    while(cin>>a>>b)
    {

        cout<<a<<" "<<b<<":";
        vector<int>v;
        for(int i=1; i<=a; i++)
        {
            if(prime[i]==0)
            {
                v.pb(i);
            }
        }
        c=2*b;
        d=v.size();
        if((d%2)!=0)
        {
            c--;
        }
        if(c>d)
        {
            for(int i=0; i<d; i++)
            {
                cout<<" "<<v[i];
            }
            cout<<endl;
        }
        else
        {
            n=(d-c);
            p=n/2;
            for(int i=p; i<c+p ; i++)
            {
                cout<<" "<<v[i];
            }
            cout<<endl;
        }

    cout<<endl;

    }

}
