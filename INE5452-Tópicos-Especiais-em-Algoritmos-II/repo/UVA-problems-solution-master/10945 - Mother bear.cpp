#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long

int main()
{
//freopen("txt.txt","r",stdin);
    fast
    ll int t,a,b,c,d,e,n;
    string s;
    while(getline(cin,s))
    {
        if(s=="DONE")
            break;
        vector<char>v,v1;

        a=s.length();
        for(int i=0; i<a; i++)
        {
            if(isalpha(s[i]))
            {
                v.push_back(s[i]);
            }
        }
        transform(v.begin(),v.end(),v.begin(),::tolower);
        v1=v;
        reverse(v.begin(),v.end());
        if(v==v1)
            cout<<"You won't be eaten!"<<endl;
        else
            cout<<"Uh oh.."<<endl;
    }


}
