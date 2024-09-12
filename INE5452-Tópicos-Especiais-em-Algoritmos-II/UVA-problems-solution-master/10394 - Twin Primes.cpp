#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long
bool prime[20000010];
int tprime[20000010];
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
    //freopen("txt.txt","r",stdin);
    fast
    sieve(20000000);
    ll int t=1,a,b,c,d,i;
    for(i=3;i<=20000000 ; i+=2)
        {

            if(prime[i]==0 && prime[i+2]==0)
            {
                tprime[t++]=i;
            }
        }

    while(cin>>a)
    {

        cout<<"("<<tprime[a]<<", "<<tprime[a]+2<<")"<<endl;

    }
}
