#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,a,b,i,j,x,temp=1;
    char s[300],s1[300];
    cin>>t;
    getchar();
    while(t--)
    {
        x=0;
        gets(s);
        a=strlen(s);
        cout<<"Case "<<temp++<<": ";
        for(i=0; i<a; i++)
        {
            j=i;
            b=0;
            while(!isalpha(s[i]))
            {
                s1[b]=s[i];
                b++;
                i++;

            }
            s1[b]='\0';
            x=atoi(s1);

            while(x--)
            {
                cout<<s[j-1];
            }
        }
        cout<<endl;

    }




}
