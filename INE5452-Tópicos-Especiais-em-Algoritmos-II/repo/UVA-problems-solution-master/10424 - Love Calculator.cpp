#include<bits/stdc++.h>
using namespace std;

int damn(string s)
{
    int i,j,k,sum;

    sum=0;
    k=s.size();
    for(i=0; i<k; i++)
    {
        if(s[i]>='a' && s[i]<='z')
            sum+=s[i]-'a'+1;
        else if(s[i]>='A' && s[i]<='Z')
            sum+=s[i]-'A'+1;
    }

    return sum;
}

int sum(int n)
{
    if(n < 10)
        return n;
    int s = 0;
    while(n)
    {
        s += n%10;
        n /= 10;
    }
    return sum(s);
}
int main()
{
    string s,s1;
    int i,j,k,x,y;
    float p,q;
    while(getline(cin,s))
    {
        getline(cin,s1);
        i=damn(s);
        j=damn(s1);
        x=min(sum(i),sum(j));
        y=max(sum(i),sum(j));
        printf("%.2f %%\n", (float)x/y*100.0);

    }
}
