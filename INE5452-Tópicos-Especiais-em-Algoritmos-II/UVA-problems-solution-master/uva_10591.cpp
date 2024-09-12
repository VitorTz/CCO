#include<bits/stdc++.h>
using namespace std;

int countd(int n)
{
    if(n==0)
        return 0;
    return 1+countd(n/10);
}

int main()
{

    int n,n1,i,t,a,b,c,cs=1,temp,s;
    cin>>t;
    while(t--)
    {
        cin>>n;
        n1=n;
        if(n1==1)
        {
            cout<<"Case #"<<cs++<<": "<<1<<" is a Happy number."<<endl;

        }
        else
        {
            if(n==2)
                n=4;
            if(n==3)
                n=9;
            while(1)
            {
                s=0;
                while(n!=0)
                {
                    temp=n%10;
                    s+=pow(temp,2);
                    n=n/10;
                }
                n=s;
                c=countd(s);
                if(c==1)break;
            }

            if(s==1)
                cout<<"Case #"<<cs++<<": "<<n1<<" is a Happy number."<<endl;
            else
                cout<<"Case #"<<cs++<<": "<<n1<<" is an Unhappy number."<<endl;
        }

    }

}




