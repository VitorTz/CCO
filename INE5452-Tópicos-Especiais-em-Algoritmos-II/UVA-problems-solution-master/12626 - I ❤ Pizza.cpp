#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long


int main()
{
    //freopen("txt.txt","r",stdin);
    fast

    ll int t,m,r,g,tt,a,b,c=0,d,i,j;
    string s;
    cin>>t;
    while(t--)
    {
        m=0,r=0,g=0,tt=0,a=0,i=0;
        cin>>s;
        j=s.length();
        for(int k=0;k<j;k++)
        {
            if(s[k]=='M')
            {
                m++;
            }
            else if(s[k]=='A')
            {
                a++;
            }
            else if(s[k]=='R')
            {
                r++;
            }
            else if(s[k]=='G')
            {
                g++;
            }
            else if(s[k]=='I')
            {
                i++;
            }
            else if(s[k]=='T')
            {
                tt++;
            }
        }
        a/=3;
        r/=2;
        m=min(m,min(a,r));
        g=min(g,min(m,i));
        cout<<min(g,tt)<<endl;

    }
}
