#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("txt.txt","r",stdin);
    double a,b,c,d,e,f,a1,b1,c1,d1,sum;
    int t,cs=1;
    cin>>t;
    while(t--)
    {
        a1=0,b1=0,c1=0,d1=0;
        cin>>a;
        if(a<=180000)
        {
            cout<<"Case "<<cs++<<": "<<"0"<<endl;
        }
        else
        {
            b=a-180000;
            if(b<=300000)
            {
                a1=b*0.1;
            }
            else
            {
                a1=300000*0.1;
                c=a-(180000+300000);
                if(c<=400000)
                {
                    b1=c*0.15;

                }
                else
                {
                    b1=400000*0.15;
                    d=a-(180000+700000);
                    if(d<=300000)
                    {
                        c1=d*0.2;

                    }
                    else
                    {
                        c1=300000*0.2;
                        e=a-(180000+700000+300000);
                        d1=e*0.25;
                    }
                }
            }
            sum=a1+b1+c1+d1;
            if(sum<=2000)
                cout<<"Case "<<cs++<<": "<<2000<<endl;
            else
                cout<<"Case "<<cs++<<": "<<(int)ceil(sum)<<endl;
        }
    }
}
