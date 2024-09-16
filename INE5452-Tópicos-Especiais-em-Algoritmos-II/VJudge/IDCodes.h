//
// Created by vitor on 9/16/24.
//

#ifndef IDCODES_H
#define IDCODES_H
#include <algorithm>
#include <string>
#include <iostream>
#include "Solution.h"

class IDCodes : Solution {

public:
    int main(int argc, char *argv[]) override;

};

inline int IDCodes::main(int argc, char *argv[]) {
    std::string s{};
    while (true) {
        std::getline(std::cin, s);
        if (s == "#") { break; }
        if (std::next_permutation(s.begin(), s.end())) {
            std::cout << s << '\n';
        } else {
            std::cout << "No Successor\n";
        }
    }
    return 0;
}


#endif //IDCODES_H
