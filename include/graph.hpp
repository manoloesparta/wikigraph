#pragma once

#include <string>

struct Node 
{
private:
    std::string datadir;

public:
    Node(std::string datadir);
    void neighbors();
    void chooseRandom();
};