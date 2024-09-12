#include<iostream>
using namespace std;
int main()
{
    int a,t,sum=0;
    string c;
    cin>>t;
    while(t--)
    {
        cin>>c;
        if(c=="donate")
        {
            cin>>a;
            sum+=a;
        }

        else if(c=="report")
            cout<<sum<<endl;
    }
}
