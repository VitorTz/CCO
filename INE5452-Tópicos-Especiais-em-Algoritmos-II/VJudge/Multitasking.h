//
// Created by vitor on 9/16/24.
//

#ifndef MULTITASKING_H
#define MULTITASKING_H
#include "Solution.h"
#include <bitset>
#include <iostream>


class Multitasking final : public Solution {

public:
        int main(int argc, char *argv[]) override;

};

inline int Multitasking::main(int argc, char *argv[]) {
    const int limit = 1000000;
    int n, m;

    while (true){
        std::cin >> n >> m;
        if (n == 0 && m == 0) break;
        std::bitset <1000100> bSet;
        bool isValidCalendar = true;

        // One-Time task
        for (int i=0; i != n; i++){
            int start, finish;
            std::cin >> start >> finish;
            // if (isValidCalendar) {
                for (int j = start; j < finish && isValidCalendar; j++){
                    if (bSet[j]){
                        isValidCalendar = false;
                    } else {
                        bSet.flip(j);
                    }
                }
            // }
        }

        // Repeating tasks
        for (int i = 0; i != m; i++){
            int start, finish, repeat;
            std::cin >> start >> finish >> repeat;
            // if (isValidCalendar){
                for (int x = 0; start + repeat * x <= limit && isValidCalendar; x++){
                    for (int j = start; j < finish; j++){
                        const int bit = j + repeat * x;
                        if (bit > limit) break;
                        if (bSet[bit])
                            isValidCalendar = false;
                        else
                            bSet.flip(bit);
                    }
                }
            // }
        }

        if (isValidCalendar == true)
            std::cout << "NO CONFLICT" << '\n';
        else
            std::cout << "CONFLICT" << '\n';

    }
    return 0;
}


#endif //MULTITASKING_H
