#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("txt.txt","r",stdin);
    int a,b,c,d,ar[3],t,cs=1,t1;
    cin>>t;
    while(t--)
    {
        cin>>a>>b>>c>>d;
        for(int i=0;i<3;i++)
            cin>>ar[i];
        sort(ar,ar+3);
        t1=a+b+c+d+((ar[1]+ar[2])/2);
        if(t1>=90)
        {
            cout<<"Case "<<cs++<<": "<<"A"<<endl;
        }
        else if(t1>=80 && t1<90)
        {
            cout<<"Case "<<cs++<<": "<<"B"<<endl;
        }
        else if(t1>=70 && t1<80)
        {
            cout<<"Case "<<cs++<<": "<<"C"<<endl;
        }
        else if(t1>=60 && t1<70)
        {
            cout<<"Case "<<cs++<<": "<<"D"<<endl;
        }
        else if(t1<60)
        {
            cout<<"Case "<<cs++<<": "<<"F"<<endl;
        }
    }

}
