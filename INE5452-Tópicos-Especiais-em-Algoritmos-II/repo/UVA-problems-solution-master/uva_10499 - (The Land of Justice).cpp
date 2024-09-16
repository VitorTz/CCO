#include<iostream>
using namespace std;
int main()
{
    long long a,b;
    while(cin>>a)
    {
        if(a<0)break;
        if(a<=1)
            cout<<0<<"%"<<endl;
        else
            cout<<25*a<<"%"<<endl;

    }
}
