#include <iostream>
#include "graph.cpp"
#include "map"



int main() {
    std::vector<std::vector<int>> arestas = {
        {0, 5},
        {4, 3},
        {0, 1},
        {9, 12},
        {6, 4},
        {5, 4},
        {0, 2},
        {11 ,12},
        {9, 10},
        {0, 6},
        {7, 8},
        {9, 11},
        {5, 3}
    };
    Graph<int> g = Graph<int>{arestas};
    // std::cout << g.toString() << std::endl;
}