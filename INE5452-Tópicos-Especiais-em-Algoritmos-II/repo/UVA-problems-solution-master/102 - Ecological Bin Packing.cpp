#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long

int main()
{
//freopen("txt.txt","r",stdin);
    fast
    ll int t,a[10],b,c,d,e,n;
    while(cin>>a[0])
    {
        vector< pair <int,string> > v;
        for(int i=1;i<9;i++)
        {
            cin>>a[i];
        }
        b=a[3]+a[6]+a[1]+a[7]+a[2]+a[5];
        v.push_back( make_pair(b,"BGC") );
        b=a[3]+a[6]+a[2]+a[8]+a[1]+a[4];
        v.push_back( make_pair(b,"BCG") );
        b=a[4]+a[7]+a[0]+a[6]+a[2]+a[5];
        v.push_back( make_pair(b,"GBC") );
        b=a[4]+a[7]+a[2]+a[8]+a[0]+a[3];
        v.push_back( make_pair(b,"GCB") );
        b=a[5]+a[8]+a[0]+a[6]+a[1]+a[4];
        v.push_back( make_pair(b,"CBG") );
        b=a[5]+a[8]+a[1]+a[7]+a[0]+a[3];
        v.push_back( make_pair(b,"CGB") );

        sort(v.begin(),v.end());
        cout<<v[0].second<<" "<<v[0].first<<endl;
    }
}
