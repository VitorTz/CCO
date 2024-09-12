#include<bits/stdc++.h>
using namespace std;
int main()
{
    string a;
    int k,b,i,x,y,c,d,t=1;
    cin>>k;
    getchar();
    while(k--)
    {
        x=0,y=0;
        getline(cin,a);
        b=a.size();
        for(i=0;i<b;i++)
        {
            if(a[i]=='a' || a[i]=='d' || a[i]=='g' || a[i]=='j'
                || a[i]=='m' || a[i]=='p' || a[i]=='t' || a[i]=='w')
            {
                x++;
                y++;
            }
            else if(a[i]=='b' || a[i]=='e' || a[i]=='h' || a[i]=='k'
                || a[i]=='n' || a[i]=='q' || a[i]=='u' || a[i]=='x')
            {
                x++;
                y+=2;
            }
            else if(a[i]=='c' || a[i]=='f' || a[i]=='i' || a[i]=='l'
                || a[i]=='o' || a[i]=='r' || a[i]=='v' || a[i]=='y')
            {
                x++;
                y+=3;
            }
            else if(a[i]=='s' || a[i]=='z')
            {
                x++;
                y+=4;
            }

        }
        cout<<"Case #"<<t++<<": "<<y+(b-x)<<endl;
    }




}
