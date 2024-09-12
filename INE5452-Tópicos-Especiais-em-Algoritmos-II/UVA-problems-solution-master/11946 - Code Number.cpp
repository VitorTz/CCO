#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("txt.txt","r",stdin);
    char s[1000];
    int t,cs=1,l,l1,i,j,a,b,c;
    cin>>t;
    getchar();
    while(t--)
    {
        while(gets(s))
        {
            if(strlen(s)==0)
            {
                break;
            }
            for(i=0; s[i]!='\0'; i++)
            {
                if(s[i]=='0')
                    s[i]='O';
                else if(s[i]=='1')
                    s[i]='I';
                else if(s[i]=='2')
                    s[i]='Z';
                else if(s[i]=='3')
                    s[i]='E';
                else if(s[i]=='4')
                    s[i]='A';
                else if(s[i]=='5')
                    s[i]='S';
                else if(s[i]=='6')
                    s[i]='G';
                else if(s[i]=='7')
                    s[i]='T';
                else if(s[i]=='8')
                    s[i]='B';
                else if(s[i]=='9')
                    s[i]='P';

                cout<<s[i];
            }
            cout<<endl;
        }
        if(t)
            puts("");

    }
}
