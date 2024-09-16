#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{

    char s[2000000];
    int a,l,b=0,i;


    while(gets(s))
    {
        l = strlen(s);
        for(i = 0; i<l ; i++)
        {
            if(s[i]=='"')
            {
                b=b+1;
                if(b%2==0)
                {
                    cout<<"\'\'";

                }
                else if(b%2 == 1)
                {
                    cout<<"\`\`";
                }
            }
            else
            {
                cout<<s[i];
            }

        }
        cout<<"\n";

    }

}
