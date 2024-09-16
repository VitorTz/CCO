#include<bits/stdc++.h>
using namespace std;

int main()
{
    char s[10001];
    int k, ans, i;

    while (gets(s))
    {

        if (strcmp(s, "0") == 0)
            break;

        k = strlen(s);
        i = 0;
        ans = 0;
        while (k > 0)
        {
            ans += (s[i] - '0') * (pow(2, k) - 1);
            k--;
            i++;
        }
        cout<<ans<<endl;;
    }

}
