#include<iostream>
using namespace std;

void decToBinary(long long n)
{
    long long num[100000];

    int i = 0,t=0,b;
    while (n > 0)
    {

        num[i] = n % 2;
        if(num[i]==1)
        {
            t++;
        }
        n = n / 2;
        i++;
    }

    cout<<"The parity of ";
    for (int j = i - 1; j >= 0; j--)
    {
        cout << num[j];
    }
    cout<<" is "<<t<<" (mod 2)."<<endl;


}

int main()
{
    long long a;
    int t,b;
    while(cin>>a)
    {
        if(a==0)break;
        decToBinary(a);
    }


}
