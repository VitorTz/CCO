#include<iostream>
using namespace std;
int main()
{
    int a,b,c,d,l,x,i,countt;
    while(cin>>a>>b>>c>>d>>l)
    {
        countt=0;
        if(a==0&&b==0&&c==0&&d==0&&l==0)break;
        for(i=0;i<=l;i++)
        {
            x=a*(i*i)+b*i+c;
            if(x%d==0)
                countt++;
        }
        cout<<countt<<endl;
    }
}
