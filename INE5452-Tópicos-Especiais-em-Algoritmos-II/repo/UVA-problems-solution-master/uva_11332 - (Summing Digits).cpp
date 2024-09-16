#include<iostream>
using namespace std;

int f(int n) {
	if(n < 10)	return n;
	int sum = 0;
	while(n) {
		sum += n%10;
		n /= 10;
	}
	return f(sum);
}

int main()
{
    long long a;
    while(cin>>a)
    {
        if(a==0)
            break;

        cout<<f(a)<<endl;

    }
}
