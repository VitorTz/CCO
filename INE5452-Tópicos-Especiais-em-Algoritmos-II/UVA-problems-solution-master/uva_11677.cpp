#include<bits/stdc++.h>
using namespace std;

int main()
{
    int a,b,c,d,e,f,g;
    while(cin>>a>>b>>c>>d)
    {
        if(a==0&&b==0&&c==0&&d==0)break;

        if(c>a)
        {
            cout<<abs((a*60+b)-(c*60+d))<<endl;
        }
        else if(c<a)
        {
            if(b>=d)
            {
                e=24-a;
                e=e+c;
                f=abs(b-d);
                cout<<e*60-f<<endl;
            }
            else
            {
                e=24-a;
                e=e+c;
                f=abs(b-d);
                cout<<e*60+f<<endl;
            }

        }
        else if(a==c)
        {
            if(b<=d)
            {
                cout<<d-b<<endl;
            }
            else
            {
                e=b-d;
                cout<<1440-e<<endl;
            }
        }

    }
}
