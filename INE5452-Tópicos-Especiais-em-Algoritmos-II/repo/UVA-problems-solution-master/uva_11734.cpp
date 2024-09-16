#include<bits/stdc++.h>
using namespace std;

string Marge(string x)
{
    string y;
    for(int i = 0; x[i]; i++)
    {
        if(x[i] != ' ')
            y.push_back(x[i]);
    }
    return y;
}

int main()
{
    string a, b;
    int t, i,cs=1;
    cin >> t;
    getchar();
    while(t--)
    {
        getline(cin, a);
        getline(cin, b);
        if(a == b)
            cout << "Case " << cs++ << ": Yes\n";
        else
        {
            a = Marge(a);
            b = Marge(b);
            if(a == b)
                cout << "Case " << cs++ << ": Output Format Error\n";
            else
                cout << "Case " << cs++ << ": Wrong Answer\n";
        }
    }

}
