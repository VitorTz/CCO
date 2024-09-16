//
// Created by vitor on 9/16/24.
//

#ifndef THROWINGCARDSAWAY_H
#define THROWINGCARDSAWAY_H
#include <iostream>
#include <vector>
#include <queue>
#include "Solution.h"


class ThrowingCardsAway final : public Solution {

public:
    int main(int argc, char *argv[]) override;

};

inline int ThrowingCardsAway::main(int argc, char *argv[]) {
    int n;

    while (true) {
        std::cin >> n;
        if (n == 0) { break; }
        std::queue<int> q{};
        for (int i = 1; i < n+1; i++) {
            q.push(i);
        }
        std::vector<int> discardedCards{};
        discardedCards.reserve(n);
        while (q.size() >= 2) {
            discardedCards.push_back(q.front());
            q.pop();
            q.push(q.front());
            q.pop();
        }
        std::cout << "Discarded cards:";
        for (std::size_t i = 0; i < discardedCards.size(); i++) {
            std::cout << ' ' << discardedCards[i];
            if (i < discardedCards.size() - 1) {
                    std::cout << ',';
            }
        }
        std::cout << '\n';
        std::cout << "Remaining card: " << q.front() << '\n';
    }

    return 0;
}
#endif //THROWINGCARDSAWAY_H
