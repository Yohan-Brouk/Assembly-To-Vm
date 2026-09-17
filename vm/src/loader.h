#pragma once
#include <iostream>
#include <vector>

bool loader(std::ifstream &file, std::string path);
std::vector<char> copy(std::ifstream &file);