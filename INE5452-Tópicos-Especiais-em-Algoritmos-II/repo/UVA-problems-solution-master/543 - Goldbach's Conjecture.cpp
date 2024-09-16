#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long
bool prime[1000001];

void sieve( int n )
{
    int x = sqrt( n );
    prime[0] = prime[1] = 1;
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
    fast
    sieve(1000000);
    ll int t,a,b,c,d,i;
    while(cin>>a)
    {
        if(a==0)
            break;
        b=a/2+1;
        for(i=3; i<=b; i+=2)
        {
            c=a-i;
            if(prime[i]==0 && prime[c]==0)
            {
                break;
            }
        }
        
        cout<<a<<" = "<<i<<" + "<<a-i<<endl;
        
    }
}
