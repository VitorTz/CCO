#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("txt.txt","r",stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int s[10001];
    int k,a,ans, i=0;

    while (cin>>a)
    {
        k=0;
        s[i++]=a;
        sort(s,s+i);
        if(i%2==0)
        {
            k=(s[i/2]+s[i/2-1])/2;
        }
        else
        {
            k=s[i/2];
        }
        cout<<k<<endl;

    }

}
