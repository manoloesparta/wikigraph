#pragma once

#include <vector>
#include <string>

const std::string directory{ "test" };

struct Node 
{
    std::string start;
    std::vector<std::string> neighbors(std::string);

public:
    Node(std::string start);
    std::vector<std::string> run();
};