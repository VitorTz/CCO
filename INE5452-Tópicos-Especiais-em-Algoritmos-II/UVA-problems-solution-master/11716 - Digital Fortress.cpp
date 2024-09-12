#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("txt.txt","r",stdin);
    string s;
    int t,cs=1,l,l1,i,j,a,b,c;
    cin>>t;
    getchar();
    while(t--)
    {
        getline(cin,s);
        l=s.length();
        l1=sqrt(l);
        a=l1*l1;
        if(a!=l)
        {
            cout<<"INVALID"<<endl;
        }
        else
        {
            for(i=0;i<l1;i++)
            {
                for(j=i;j<l;j+=l1)
                {
                    cout<<s[j];
                }
            }
            cout<<endl;
        }


    }
}
