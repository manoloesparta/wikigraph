#include <iostream>
#include "graph.hpp"

int main()
{
    Node n{ "a" };
    n.run("b");
    std::cout << n.start << std::endl;
    return 0;
}