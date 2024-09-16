//
// Created by vitor on 9/16/24.
//

#ifndef EXHIBITION_H
#define EXHIBITION_H
#include "Solution.h"
#include <cstdio>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <array>


class Exhibition final : public Solution {

public:
    int main(int argc, char *argv[]) override;

};


inline int Exhibition::main(int argc, char *argv[]) {
    int n;
    std::unordered_map<int, std::unordered_set<int>> m{};
    std::array<int, 50> friendsArray{};
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        m.clear();
        int friends;
        std::cin >> friends;

        for (int j = 0; j < friends; j++) {
            friendsArray[j] = 0;
            int numStamps;
            std::cin >> numStamps;
            for (int x = 0; x < numStamps; x++) {
                int stampType;
                std::cin >> stampType;
                m[stampType].insert(j);
            }
        }
        double totalUniques = 0;
        for (auto& pair : m) {
            if (pair.second.size() == 1) {
                friendsArray[*pair.second.begin()] += 1;
                totalUniques += 1.0;
            }
        }
        printf("Case %d:", i+1);
        for (int x = 0; x < friends; x++) {
            printf(" %.6lf%%", static_cast<double>(friendsArray[x]) / totalUniques * 100.0);
        }
        printf("\n");
    }
    return 0;
}


#endif //EXHIBITION_H
