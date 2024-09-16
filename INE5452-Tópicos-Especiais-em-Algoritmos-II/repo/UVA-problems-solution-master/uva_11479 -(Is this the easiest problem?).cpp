#include<iostream>
using namespace std;

int main()
{
    long long a,b,c,t,cs=1;
    cin>>t;
    while(t--)
    {
        cin>>a>>b>>c;
        if(a+b<=c || b+c<=a || a+c<=b)
        {
            cout<<"Case "<<cs++<<": "<<"Invalid"<<endl;
        }
        else
        {
            if(a==b && b==c)
                cout<<"Case "<<cs++<<": "<<"Equilateral"<<endl;
            else if(a==b || b==c || a==c)
                cout<<"Case "<<cs++<<": "<<"Isosceles"<<endl;

            else
                cout<<"Case "<<cs++<<": "<<"Scalene"<<endl;
        }

    }
}
