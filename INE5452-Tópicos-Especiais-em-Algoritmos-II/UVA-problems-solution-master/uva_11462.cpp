#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll int ar[2000005];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll int n,i;

    while(cin>>n)
    {
        if(n==0)
            break;
        for(i=0; i<n; i++)
        {
            cin>>ar[i];
        }
        sort(ar,ar+n);
        for(int j=0;j<n;j++)
        {
            cout<<ar[j];
            if(j<(n-1))
                cout<<" ";
        }
        cout<<endl;

    }

}



