#include <iostream>
#include <stdio.h>


float f_to_celcius(int f) {    
    return (5.0f * f) / 9.0f;
}


int main(int argc, char const *argv[]) {
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int c, f;
        std::cin >> c >> f;
        float r = c + f_to_celcius(f);
        printf("Case %d: %.2f\n", i + 1, r);
    }
    return 0;
}
