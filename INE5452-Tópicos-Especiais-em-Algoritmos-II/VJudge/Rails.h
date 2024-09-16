//
// Created by vitor on 9/16/24.
//

#ifndef STACK_H
#define STACK_H
#include <iostream>
#include <stack>
#include "Solution.h"



class Rails final : public Solution {


    public:
        int main(int argc, char *argv[]) override;

};


inline int Rails::main(int argc, char *argv[]) {
    while (true) {
        int n;
        std::cin >> n;
        if (n == 0) { break; }

        while (true) {
            std::stack<int> stack{};

            int a;
            int k = 0;
            for (int i = 0; i < n; i++) {
                std::cin >> a;
                if (a == 0) { break; }
                while (k < n && k != a) {
                    if (!stack.empty() && stack.top() == a) {
                        break;
                    }
                    stack.push(++k);
                }

                if (stack.top() == a) {
                    stack.pop();
                }

            }

            if (a == 0) { break; }

            if (stack.empty()) {
                std::cout << "Yes\n";
            } else {
                std::cout << "No\n";
            }
        }

        std::cout << '\n';
    }
    return 0;
}


#endif //STACK_H
