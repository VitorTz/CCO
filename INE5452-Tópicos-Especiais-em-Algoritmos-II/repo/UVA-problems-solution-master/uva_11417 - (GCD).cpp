#include<iostream>
using namespace std;
int gcd(int a,int b)
{
    return b==0?a:gcd(b,a%b);
}

int main()
{
    //freopen("txt.txt","r",stdin);
    int j,G,i,d,N;
    while(cin>>N)
    {
        if(N==0)break;
        G=0;
        for(i=1; i<N; i++)
            for(j=i+1; j<=N; j++)
            {
                G+=gcd(i,j);
            }

        cout<<G<<endl;

    }
}
