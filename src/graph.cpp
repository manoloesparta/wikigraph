#include "graph.hpp"
#include <string>
#include <stack>
#include <map>

Node::Node(std::string start) : start{ start }
{}

std::vector<std::string> Node::neighbors(std::string vertex)
{
    return std::vector<std::string>{};
}

std::vector<std::string> Node::run()
{
    std::map<std::string, int> history{};
    std::stack<std::string> stack{};
    stack.push(start);

    while (history.size() > 0)
    {
        std::string vertex{ stack.top() };
        stack.pop();
        
        if(history.count(vertex) != 1)
        {
            history[vertex] = 1;
            for(std::string one : neighbors(vertex))
            {
                stack.push(one);
            }
        }
    }
    
    return std::vector<std::string>{};
}