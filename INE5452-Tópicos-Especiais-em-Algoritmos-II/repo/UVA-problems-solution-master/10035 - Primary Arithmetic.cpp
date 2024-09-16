#include <bits/stdc++.h>
using namespace std;

int result(int a,int b)
{
    int x,s=0,t=0;
    while (a||b) {
        s=((a%10)+(b%10)+s)/10;
        a= a / 10;
        b=b/10;
        t+=s;

    }
    return t;
}


int main()
{
    //freopen("txt.txt","r",stdin);
    int a,b,c,d;
    while(cin>>a>>b, a||b)
    {
        if(result(a,b)==0)
            cout<<"No carry operation."<<endl;
        else if(result(a,b)==1)
            cout<<"1 carry operation."<<endl;
        else
            cout<<result(a,b)<<" carry operations."<<endl;
    }
}
