#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("txt.txt","r",stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int s;
    int k,a,b,c,d,n,i,y;
    while(cin>>a>>b>>c>>d)
    {
        y=b+1;
        while (c--)
        {
            n=0;

            cin>>k;
            for(i=1; i<=d; i++)
            {
                cin>>s;
                n=max(s,n);

            }
            if(n>=a)
            {
                y=min(y,a*k);
            }

        }

        if(y==b+1)
            cout<<"stay home"<<endl;
        else
            cout<<y<<endl;


    }


}
