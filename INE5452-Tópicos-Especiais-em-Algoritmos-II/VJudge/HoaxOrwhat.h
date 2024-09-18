//
// Created by vitor on 9/17/24.
//

#ifndef HOAXORWHAT_H
#define HOAXORWHAT_H
#include "Solution.h"
#include <iostream>
#include <set>

class HoaxOrWhat final : public Solution {

public:
    int main(int argc, char *argv[]) override;

};


inline int HoaxOrWhat::main(int argc, char *argv[]) {
    int days;
    while (true) {
        std::cin >> days;
        if (days == 0) { break; }
        std::multiset<std::size_t> multiSet{};
        std::size_t totalPaid = 0;
        int k, m;
        for (int i = 0; i < days; i++) {
            std::cin >> k;
            int j;
            for (j = 0; j < k; j++) {
                std::cin >> m;
                multiSet.insert(m);
            }
            // end of day(i)
            const std::size_t minBil =  *(multiSet.lower_bound(0));
            const std::size_t maxBil = *(--multiSet.end());
            totalPaid += maxBil - minBil;
            std::size_t c = multiSet.erase(minBil);
            for (j = 0; j < c - 1; j++) {
                multiSet.insert(minBil);
            }
            c = multiSet.erase(maxBil);
            for (j = 0; j < c - 1; j++) {
                multiSet.insert(maxBil);
            }
        }
        // end of all days
        std::cout << totalPaid << '\n';
    }
    return 0;
}



#endif //HOAXORWHAT_H
