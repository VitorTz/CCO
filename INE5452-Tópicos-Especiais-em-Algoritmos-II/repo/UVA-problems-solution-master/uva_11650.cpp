#include<bits/stdc++.h>
using namespace std;

int main()
 {
    int t, h, m;
    cin>>t;
    while(t--)
    {
        scanf("%d:%d", &h, &m);
        h= 11-h;
        if (m == 0)
        {
            h+=1;
        }
        if(h <= 0)
            h=h+12;
        if(m!= 0)
            m= 60-m;
        printf("%02d:%02d\n",h,m);
    }
}
