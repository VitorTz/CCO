#include<bits/stdc++.h>
using namespace std;

int main()
{
    string id;
    
    while (cin >> id, id != "#")
    {
        if (next_permutation(id.begin(), id.end()))
            cout<<id<<endl;
        else
            cout<<"No Successor\n";
    }
}
