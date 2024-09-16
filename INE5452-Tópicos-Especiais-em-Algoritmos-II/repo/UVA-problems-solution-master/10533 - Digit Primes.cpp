#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long
bool prime[1000001];
int tprime[1000001];
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

int sum_digit(int x)
{
    int s=0;
    while(x!=0)
    {
        s+=(x%10);
        x/=10;
    }
    return s;
}
int main()
{
    //freopen("txt.txt","r",stdin);
    fast
    sieve(1000000);
    ll int t,a,b,c=0,d,i;
    cin>>t;
    for(i=0; i<=1000000; i++)
    {

        if(prime[i]==0 && prime[sum_digit(i)]==0)
        {
            c++;
        }
        tprime[i]=c;
    }
    while(t--)
    {
        c=0;
        cin>>a>>b;
        cout<<tprime[b]-tprime[a-1]<<endl;

    }


}
