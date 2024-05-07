#include "graph.h"
#include <map>


template<typename T>
Graph<T>::Graph(int VV, int EE) {
    this->V = VV;
    this->E = EE;
    this->adjs = std::vector<std::vector<T>> (this->V);
}

template<typename T>
Graph<T>::Graph(int VV, std::vector<std::vector<T>>& arestas) : Graph<T>(VV, arestas.size()) {
    for (std::vector<T>& aresta : arestas) {
        this->add_edge(aresta);
    }
}

template<typename T>
Graph<T>::Graph(std::vector<std::vector<T>>& arestas) : Graph<T>(this->count_vertices(arestas), arestas) { }

template<typename T>
int Graph<T>::count_vertices(std::vector<std::vector<T>>& arestas) {
    std::map<T, int> m;
    for (std::vector<T>& aresta : arestas) {
        for (T& value : aresta) {
            m.insert(std::pair<T, int>(value, 0));
        }
    }
    return m.size();
}

template<typename T>
void Graph<T>::add_key(T v) {
    this->keys.find(v);
}

template<typename T>
int Graph<T>::get_key(T v) {
    int i = this->keys.size();
    this->keys.insert(
        std::pair<T, int>(v, i)
    );
    return this->keys.at(v);
}

template<typename T>
void Graph<T>::add_edge(T u, T  v) {
    int u_i = this->get_key(u);
    int v_i = this->get_key(v);
    this->adjs[u_i].push_back(v);
    this->adjs[v_i].push_back(u);
}

template<typename T>
void Graph<T>::add_edge(std::vector<T>& aresta) {
    this->add_edge(aresta[0], aresta[1]);
}

template<typename T>
int Graph<T>::getV() { return this->V; }

template<typename T>
int Graph<T>::getE() { return this->E; }

template<typename T>
std::vector<T>* Graph<T>::adj(T u) {
    return &this->adjs[this->get_key(u)];
}