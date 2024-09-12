#include<iostream>
using namespace std;
int main()
{
    //freopen("txt.txt","r",stdin);
    int ar[20],i,d;
    int t,n,cs=1;
    cin>>t;
    while(t--)
    {
        cin>>n;
        if(n%2==0)d=(n/2)-1;
        else{d=n/2;}
        for(i=0;i<n;i++)
        {
            cin>>ar[i];
        }
        cout<<"Case "<<cs++<<": "<<ar[d]<<endl;

    }
}
