#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("txt.txt","r",stdin);
    float a,b,c,d,t,sum,e,f;
    int cs=1;
    while(cin>>a)
    {
        if(a==0)
            break;

        cout<<fixed;
        cout<<setprecision(3);
        if(a==1)
        {
            cin>>b>>c>>d;
            e=(c-b)/d;
            f=(d*(b+c))/2;

            cout<<"Case "<<cs++<<": "<<f<<" "<<e<<endl;
        }
        else if(a==2)
        {
            cin>>b>>c>>d;
            e=(c-b)/d;
            f=(e*(b+c))/2;
            cout<<"Case "<<cs++<<": "<<f<<" "<<e<<endl;
        }
        else if(a==3)
        {
            cin>>b>>c>>d;
            e=sqrt((b*b)+2*c*d);
            f=(e-b)/c;
            cout<<"Case "<<cs++<<": "<<e<<" "<<f<<endl;
        }
        else if(a==4)
        {
            cin>>b>>c>>d;
            e=sqrt((b*b)-2*c*d);
            f=(b-e)/c;
            cout<<"Case "<<cs++<<": "<<e<<" "<<f<<endl;
        }

    }
}
