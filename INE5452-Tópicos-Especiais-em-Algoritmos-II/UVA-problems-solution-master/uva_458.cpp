#include<bits/stdc++.h>
using namespace std;
int main()
{
    char a[1000];
    int l;
    while(gets(a))
    {
        l=strlen(a);
        for(int i=0;i<l;i++)
        {
            printf("%c", a[i]-7);
        }
        cout<<endl;
    }

}



