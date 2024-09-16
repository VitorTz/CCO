#include<bits/stdc++.h>
using namespace std;
int main()
{

    int n,i,cs=1,t,m,a;

    while(cin>>n)
    {
        t=0;
        m=1;
        if(n<0)
            break;

        if(n==1)
        {
            cout<<"Case "<<cs++<<": "<<0<<endl;
        }
        else
        {
            while(1)
            {
                m=m*2;
                t++;

                if(m>=n)
                    break;

            }
            cout<<"Case "<<cs++<<": "<<t<<endl;
        }


    }

}




