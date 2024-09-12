#include<bits/stdc++.h>
using namespace std;
int main()
{
    int ar[3],cs=1,t;
    cin>>t;
    while(t--)
    {
        for(int i=0; i<3; i++)
        {
            cin>>ar[i];
        }
        sort(ar,ar+3);
        cout<<"Case "<<cs++<<": "<<ar[1]<<endl;
    }


}
