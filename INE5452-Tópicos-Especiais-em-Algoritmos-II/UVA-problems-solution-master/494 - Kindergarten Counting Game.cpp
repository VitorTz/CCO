#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long
#define pb push_back

int main()
{
//freopen("txt.txt","r",stdin);
    fast
    ll int t,a,b,c,d,e,n;
    string s;
    while(getline(cin,s))
    {
        b=0;
        a=s.length();
        for(int i=0;i<a;i++)
        {
            if(isalpha(s[i]) && !isalpha(s[i+1]))
            {
                b++;
            }
        }
        cout<<b<<endl;

    }
}
