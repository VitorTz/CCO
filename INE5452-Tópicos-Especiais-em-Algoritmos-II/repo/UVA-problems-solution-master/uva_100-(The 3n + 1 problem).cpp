#include<iostream>
using namespace std;
int main()
{
    int a,b,c,d,i,j,temp,bomb,x,y;
    while((cin>>a>>b) && a>0&&b>0)
    {
        x=a;
        y=b;
        if(a>b)
        {
            bomb=a;
            a=b;
            b=bomb;
        }
        d=0;

        for(i=a; i<=b; i++)
        {
            j=i;
            temp=1;
            while(j!=1)
            {
                if(j%2==0)
                {
                    j=j/2;
                }
                else
                {
                    j=(3*j)+1;

                }
                temp++;
            }
            if(temp>d)
                d=temp;


        }
        cout<<x<<" "<<y<<" "<<d<<endl;
    }



}
