//
// Created by vitor on 9/18/24.
//

#ifndef CONTESTSCOREBOARD_H
#define CONTESTSCOREBOARD_H
#include <iostream>
#include <string>
#include <sstream>
#include <array>
#include <algorithm>
#include <bitset>
#include "Solution.h"


class ContestScoreboard final : public Solution {

public:
    int main(int argc, char *argv[]) override;

};


typedef struct contest {
    int teamNumber{};
    int numProblemsSolved{};
    int penalty{};
    bool isValidContestant{};
    std::bitset<10> correctAttempt{};
    std::array<int, 10> incorrectAttempts{};
} contest_t;

inline int ContestScoreboard::main(int argc, char *argv[]) {
    int n, j;
    std::cin >> n;
    std::cin.ignore();
    std::cin.ignore();

    for (int i = 0; i < n; i++) {
        std::array<contest_t, 101> arr{};
        for (j = 0; j < 101; j++) {
            arr[j].teamNumber = j;
        }

        std::string s;
        while (std::getline(std::cin, s) && s.empty() == false) {
            std::stringstream sStream(s);
            int contestant, problem, time;
            char L;
            sStream >> contestant >> problem >> time >> L;
            contest_t* cont = &arr[contestant];
            cont->isValidContestant = true;
            if (L == 'I') {
                cont->incorrectAttempts[problem]++;
            } else if (L == 'C' && cont->correctAttempt[problem] == false) {
                cont->correctAttempt.set(problem, true);
                cont->numProblemsSolved++;
                cont->penalty += time + cont->incorrectAttempts[problem] * 20;
            }

        }
        std::sort(
            arr.begin(),
            arr.end(),
            [](const contest_t& l, const contest_t& r) {
                if (l.isValidContestant && r.isValidContestant) {
                    if (l.numProblemsSolved != r.numProblemsSolved)
                        return l.numProblemsSolved > r.numProblemsSolved;
                    if (l.penalty != r.penalty)
                        return l.penalty < r.penalty;
                    return l.teamNumber < r.teamNumber;
                }
                return l.isValidContestant > r.isValidContestant;
            }
        );

        for (j = 0; j < 101; j++) {
            const contest_t* c = &arr[j];
            if (c->isValidContestant) {
                std::cout << c->teamNumber << ' ' << c->numProblemsSolved << ' ' << c->penalty << '\n';
            }
        }
        if (i != n - 1) {
            std::cout << '\n';
        }

    }

    return 0;
}


#endif //CONTESTSCOREBOARD_H
