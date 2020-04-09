#pragma once

#include <vector>
#include <string>

const std::string directory{ "test" };

class Node 
{
private:
    std::string start;
    std::vector<std::string> neighbors(std::string vertex);
    std::vector<std::string> split(std::string input, std::string substr);
    std::string choose(std::vector<std::string> options);

public:
    Node(std::string start);
    std::vector<std::string> run(std::string goal);
};