#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long a,b,c,sum,i;
    while(cin>>a)
    {
        sum=0;
        if(a==0)break;

        for(i=a;i>0;i--)
        {
            sum+=i*i;
        }
        cout<<sum<<endl;
    }

}



