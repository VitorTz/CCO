#include<bits/stdc++.h>
using namespace std;
int main()
{
    
    int t;
    string s;

    cin>>t;
    while (t--)
    {
        cin>>s;

        int l = s.size();

        if (s[l-1] == '5' && s[l - 2] == '3')
            cout<<"-"<<endl;
        else if (s[0] == '9' && s[l- 1] == '4')
            cout<<"*"<<endl;
        else if (s[0] == '1'  && s[1] == '9' && s[2] == '0' )
            cout<<"?"<<endl;
        else
            cout<<"+"<<endl;


    }


}
