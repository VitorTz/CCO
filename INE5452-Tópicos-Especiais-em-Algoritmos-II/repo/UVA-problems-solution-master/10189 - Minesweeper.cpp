#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long
#define pb push_back

int main()
{
//freopen("txt.txt","r",stdin);
    fast
    ll int t,a,b,c,d,e,n=1;
    string s;
    while(cin>>a>>b)
    {

        if(a==0&&b==0)break;
        if (n > 1)
            cout << endl;
        char ar[a+1][b+1];

        for(int k=0;k<a;k++)
        {
            for(int l=0;l<b;l++)
            {
                cin>>ar[k][l];
            }
        }
        cout<<"Field #"<<n++<<":"<<endl;
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                if(ar[i][j]=='*')
                {
                    cout<<'*';
                }
                else
                {
                    e=0;
                    if(ar[i][j+1]=='*')
                    {
                        e++;
                    }
                    if(ar[i][j-1]=='*')
                    {
                        e++;
                    }
                    if(ar[i+1][j]=='*')
                    {
                        e++;
                    }
                    if(ar[i-1][j]=='*')
                    {
                        e++;
                    }
                    if(ar[i-1][j-1]=='*')
                    {
                        e++;
                    }
                    if(ar[i-1][j+1]=='*')
                    {
                        e++;
                    }
                    if(ar[i+1][j-1]=='*')
                    {
                        e++;
                    }
                    if(ar[i+1][j+1]=='*')
                    {
                        e++;
                    }
                    cout<<e;

                }

            }
            cout<<endl;
        }


    }
}
