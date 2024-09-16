#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,c,d,t,sum;
    cin>>t;
    while(t--)
    {
        sum=0;
        cin>>a>>b>>c;
        a=a+b;
        while(a>=c)
        {
            sum=sum+(a/c);
            a=a%c+a/c;
        }
        cout<<sum<<endl;
    }
}
