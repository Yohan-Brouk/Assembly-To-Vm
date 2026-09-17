#include "loader.h"
#include <fstream>
#include <iostream>
#include <vector>

bool loader(std::ifstream &file, std::string path){

    file.open(path, std::ios::binary);

    if (file.is_open()){
        return true;
    } 
    else{
        return false;
    }

}

std::vector<char> copy(std::ifstream &file){
    
    std::vector<char> buffer;

    file.seekg(0, std::ios::end);
    int size = file.tellg();
    file.seekg(0, std::ios::beg);

    buffer.resize(size);

    file.read(buffer.data(), size);

    return buffer;
}