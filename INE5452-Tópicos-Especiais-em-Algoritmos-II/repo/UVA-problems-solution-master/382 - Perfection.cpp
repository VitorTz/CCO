#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("txt.txt","r",stdin);
    int a,t,i,b,n,sum,d;
    cout<<"PERFECTION OUTPUT"<<endl;
    while(cin>>a)
    {
        if(a==0 || a>60000)
            break;
        sum=0;
        n=a;
        d=a/2;
        for(i=1; i<=d; i++)
        {
            if(a%i==0)
            {
                sum+=i;
            }

        }

        if(sum==n)
            printf("%5d  PERFECT\n",n);
        if(sum<n)
            printf("%5d  DEFICIENT\n",n);
        if(sum>n)
            printf("%5d  ABUNDANT\n",n);
    }
    cout<<"END OF OUTPUT"<<endl;

}
