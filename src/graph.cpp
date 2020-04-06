#include <map>
#include <stack>
#include <vector>
#include <string>
#include <fstream>
#include "graph.hpp"

const static std::string dir{ "../test/" };

Node::Node(std::string start) : start{ start }
{}

std::vector<std::string> Node::split(std::string input, std::string substr)
{
    int pos = 0;
    std::string token;
    std::vector<std::string> result{};
    
    while ((pos = input.find(substr)) != std::string::npos) {
        token = input.substr(0, pos);
        result.push_back(token);
        input.erase(0, pos + substr.length());
    }

    result.push_back(input);
    return result;
}

std::vector<std::string> Node::neighbors(std::string vertex)
{
    std::ifstream input{ dir + vertex };
    std::string text{ std::istreambuf_iterator<char>(input), std::istreambuf_iterator<char>() };

    return split(text, ",\n");
}

std::vector<std::string> Node::run(std::string goal)
{
    std::vector<std::string> result{};
    std::map<std::string, int> hist{};
    std::stack<std::string> stack{};

    stack.push(start);
    result.push_back(start);

    while(!stack.empty())
    {
        std::string vertex{ stack.top() };
        stack.pop();

        if(hist[vertex] != 1)
        {
            hist[vertex] = 1;
            result.push_back(vertex);

            std::vector<std::string> adj{ neighbors(vertex) };
            for(std::string edge : adj)
            {
                if(edge == goal)
                {
                    result.push_back(goal);
                    return result;
                }
                stack.push(edge);
            }
            result.pop_back();
        }
    }

    return std::vector<std::string>{""};
}