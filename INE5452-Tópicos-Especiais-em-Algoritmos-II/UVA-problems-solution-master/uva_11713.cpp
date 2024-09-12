#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,i,j,l1,l2,test,test1;
    string a,b,c;
    cin>>t;
    getchar();
    while(t--)
    {
        test=0;
        test1=0;
        cin>>a>>b;
        l1=a.size();
        l2=b.size();
        if(l1!=l2)
        {
            cout<<"No"<<endl;
        }
        else
        {
            for(i=0; i<l1; i++)
            {
                if(a[i]=='a' || a[i]=='e' || a[i]=='i' || a[i]=='o' || a[i]=='u')
                {
                    a[i]='a';
                }
            }
            for(i=0; i<l1; i++)
            {
                if(b[i]=='a' || b[i]=='e' || b[i]=='i' || b[i]=='o' || b[i]=='u')
                {
                    b[i]='a';
                }
            }
            if(a==b)
                cout<<"Yes"<<endl;
            else
                cout<<"No"<<endl;

        }

    }
}

