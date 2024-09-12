#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long
#define pb push_back

int main()
{
//freopen("txt.txt","r",stdin);
    fast
    ll int t,a,b,c,d,e,n=1;
    while(cin>>a)
    {
        ll int ar[a+1];
        c=0,d=0;
        if(a==0)
        {
            break;
        }

        for(int i=0; i<a; i++)
        {
            cin>>ar[i];
            c+=ar[i];
        }
        cout<<"Set #"<<n++<<endl;
        c/=a;
        for(int j=0;j<a;j++)
        {
            if(ar[j]>c)
            {
                d+=(ar[j]-c);
            }
        }
        cout<<"The minimum number of moves is "<<d<<".\n"<<endl;

    }

}
