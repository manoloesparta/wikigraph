#include <iostream>
#include "graph.hpp"

int main()
{
    Node n{ "a" };
    auto route = n.run("d");
    for(auto a : route)
        std::cout << a << " ";
    return 0;
}