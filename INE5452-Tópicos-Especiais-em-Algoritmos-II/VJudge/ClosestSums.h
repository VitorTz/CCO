//
// Created by vitor on 9/16/24.
//

#ifndef CLOSESTSUMS_H
#define CLOSESTSUMS_H
#include "Solution.h"
#include <algorithm>
#include <array>
#include <set>
#include <vector>
#include <iostream>


class ClosestSums : public Solution {


public:
    int main(int argc, char *argv[]) override;

};

inline int ClosestSums::main(int argc, char *argv[]) {
    int n, m, i;
    int numCase = 1;
    while (true) {
        std::cin >> n;
        if (n == 0) { break; }

        std::set<int> sums{};
        std::vector<int> v{};
        v.reserve(n);
        for (i = 0; i < n; i++) {
            std::cin >> v[i];
        }

        for (i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                sums.insert(v[i] + v[j]);
            }
        }

        std::cin >> m;
        std::cout << "Case " << numCase++ << ':' << '\n';
        for (i = 0; i < m; i++) {
            int diff = 10000000;
            int query;
            std::cin >> query;
            int closeSum = query;

            std::array<std::set<int>::iterator, 3> nums{};
            nums[1] = sums.lower_bound(query);
            nums[0] = nums[2] = nums[1];
            --nums[0]; --nums[2];

            for (int j = 0; j < 3; j++) {
                if (nums[j] != sums.end() && std::abs(query - *nums[j]) < diff) {
                    diff = std::abs(query - *nums[j]);
                    closeSum = *nums[j];
                }
            }
            std::cout << "Closest sum to " << query << " is " << closeSum << '.' << '\n';
        }
    }
    return 0;
}


#endif //CLOSESTSUMS_H
