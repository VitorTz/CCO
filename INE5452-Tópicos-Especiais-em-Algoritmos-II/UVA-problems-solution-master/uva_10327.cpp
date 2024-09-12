#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i,j,n,a[1000],cs;
    while(cin>>n)
    {
        cs=0;
        for(int x=0; x<n; x++)
        {
            cin>>a[x];
        }
        for(i = 1; i<n; i++)
            for(j = 0; j<i; j++)
                if(a[j]>a[i])
                    cs++;

        cout<<"Minimum exchange operations : "<<cs<<endl;
    }

}
