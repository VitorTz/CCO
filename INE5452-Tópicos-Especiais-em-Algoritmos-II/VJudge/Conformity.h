//
// Created by vitor on 9/16/24.
//

#ifndef CONFORMITY_H
#define CONFORMITY_H
#include "Solution.h"
#include <algorithm>
#include <map>
#include <array>
#include <iostream>


class Conformity final : public Solution {

public:
    int main(int argc, char *argv[]) override;
};

inline int Conformity::main(int argc, char *argv[]) {
    int n;
    while (true) {
        std::cin >> n;
        if (n == 0) { break; }
        std::map<std::array<int, 5>, int> courseCountMap{};
        int max = 1;

        for (int i = 0; i < n; i++) {
            std::array<int, 5> arr{};
            for (int j = 0; j < 5; j++) {
                std::cin >> arr[j];
            }
            std::sort(arr.begin(), arr.end());
            courseCountMap[arr]++;
            max = std::max(max, courseCountMap[arr]);
        }

        int count = 0;
        for (auto& pair : courseCountMap) {
            if (pair.second == max) {
                count += pair.second;
            }
        }
        std::cout << count << '\n';

    }
    return 0;
}


#endif //CONFORMITY_H
