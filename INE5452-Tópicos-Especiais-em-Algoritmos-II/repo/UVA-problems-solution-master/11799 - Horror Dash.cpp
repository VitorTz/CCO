#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("txt.txt","r",stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int a[10000],cs=1,t,i,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
        }
        sort(a,a+n);
        cout<<"Case "<<cs++<<": "<<a[n-1]<<endl;
    }

}
