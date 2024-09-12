#include<bits/stdc++.h>
using namespace std;

int main()
{
//freopen("txt.txt","r",stdin);
    set<string>s;
    int i,l;
    char ar[205];
    while(gets(ar))
    {
        string x="";
        l=strlen(ar);
        for(i=0; i<=l; i++)
        {
            if(isalpha(ar[i]))
                x+=tolower(ar[i]);
            else if(x!="")
            {
                s.insert(x);
                x="";
            }
        }
    }
    for(string y:s)
    {
        cout<<y<<endl;
    }

}
