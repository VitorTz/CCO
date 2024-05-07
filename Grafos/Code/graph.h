#include <iostream>
#include <vector>
#include <map>


template <typename T>
class Graph{

private:
    int V, E;
    std::map<T, int> keys;
    std::vector<std::vector<T>> adjs;
    void add_key(T v);
    int get_key(T v);
    int count_vertices(std::vector<std::vector<T>>& arestas);

public:
    Graph(int VV, int EE);
    Graph(int VV, std::vector<std::vector<T>>& arestas);
    Graph(std::vector<std::vector<T>>& arestas);
    int getV();
    int getE();
    std::vector<T>* adj(T u);
    void add_edge(T u, T v);
    void add_edge(std::vector<T>& aresta);
    int d(T v);
    std::string toString();
};






