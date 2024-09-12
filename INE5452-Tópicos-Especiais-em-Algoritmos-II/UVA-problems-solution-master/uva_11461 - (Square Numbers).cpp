#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,i,c,temp;
    float t,d;
    while(cin>>a>>b)
    {
        temp=0;
        if(a==0&&b==0)break;
        if(a>b)
            swap(a,b);
        for(i=a;i<=b;i++)
        {
            c=sqrt(i);
            t=sqrt(i);
            d=t-c;
            if(d==0)
            {
                temp++;
            }
        }
        cout<<temp<<endl;
    }
}
