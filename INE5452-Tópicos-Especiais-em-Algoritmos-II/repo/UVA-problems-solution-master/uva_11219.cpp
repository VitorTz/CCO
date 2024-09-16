#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("txt.txt","r",stdin);
    int a,t,b,c,d,e,f;
    int ag,cs=1;
    string s;
    cin>>t;
    while(t--)
    {
        scanf("%d/%d/%d", &a, &b, &c);
        scanf("%d/%d/%d", &d, &e, &f);
        ag=c-f;
        if(e>b){ag--;}

        if(e==b && d>a){ag--;}

        if(ag<0)
        {
            cout<<"Case #"<<cs++<<": "<<"Invalid birth date"<<endl;
        }
        else if(ag>130)
        {
            cout<<"Case #"<<cs++<<": "<<"Check birth date"<<endl;
        }
        else
        {
            cout<<"Case #"<<cs++<<": "<<ag<<endl;
        }
    }

}
