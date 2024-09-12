#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long a,b,c,d,i;
    while(cin>>a>>b)
    {
        if(a<0 && b<0)break;
        if(a>b)
            swap(a,b);
        c=abs(b-a);
        d=abs(100-b+a);
        cout<<min(c,d)<<endl;

    }

}



