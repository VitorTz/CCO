#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

#define CORRECT "You won't be eaten!"
#define INCORRECT "Uh oh.."
#define DONE "DONE"


int main() {
    std::string s;

    while(getline(std::cin,s)) {
        if (s == DONE) {
            break;
        }
        std::vector<char> v1, v2;
        
        for(int i = 0; i < s.size(); i++) {
            const char c = s[i];
            if (isalpha(c)) {
                v1.push_back(c);
            }
        }        
        
        std::transform(
            v1.begin(),
            v1.end(),
            v1.begin(), 
            ::tolower
        );
        v2 = v1;
        std::reverse(v1.begin(), v1.end());
        
        if(v1 == v2) {
            std::cout << CORRECT << '\n';
        } else {
            std::cout << INCORRECT << '\n';
        }            
    }


}