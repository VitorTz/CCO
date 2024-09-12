#include<bits/stdc++.h>

using namespace std;
int main()
{
   int a,b,c,i,t;
   cin>>t;
   while(t--)
   {
       cin>>a;
       b=(((((a*567)/9)+7492)*235)/47)-498;
       i=b/10;
       cout<<abs(i%10)<<endl;
   }
}
