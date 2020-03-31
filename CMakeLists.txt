cmake_minimum_required(VERSION 3.0)

project(Wikigraph VERSION 0.1 LANGUAGES CXX)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_STANDARD 17)

include_directories(include)

add_executable(wiki main.cpp src/graph.cpp)