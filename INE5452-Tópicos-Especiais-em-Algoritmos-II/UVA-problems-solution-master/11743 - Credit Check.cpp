#include<bits/stdc++.h>
using namespace std;

int f(int n)
{
    if(n < 10)
        return n;
    int sum = 0;
    while(n)
    {
        sum += n%10;
        n /= 10;
    }
    return f(sum);
}
int daisypu(int x)
{
    int s1=0,s=0,s2=0,s3=0;
    s+=x%10;
    x=x/10;
    s1=(x%10)*2;
    s1=f(s1);
    x=x/10;
    s3=x%10;
    x=x/10;
    s2=x*2;
    s2=f(s2);
    return s+s1+s2+s3;
}
int main()
{
    //freopen("txt.txt","r",stdin);
    int a,b,c,d,t,sum;
    cin>>t;
    while(t--)
    {
        cin>>a>>b>>c>>d;
        sum=daisypu(a)+daisypu(b)+daisypu(c)+daisypu(d);

        if(sum%10==0)
            cout<<"Valid"<<endl;
        else
            cout<<"Invalid"<<endl;

    }

}
