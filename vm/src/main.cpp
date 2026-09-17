#include <iostream>
#include <fstream>
#include <vector>
#include "loader.h"
#include "vm.h"

int main(int argc, char *argv[]){

    if (argc != 2){
        std::cout << "Usage : ./vm {fichier.bin}" << std::endl; 
        return 1;
    }

    std::ifstream file;

    if(loader(file, argv[1])){
        std::cout << "The file is open" << std::endl;
        std::vector<char> buffer = copy(file);

        for (size_t i = 0; i < buffer.size(); i++) {
           std::cout << std::hex << (int)buffer[i] << std::endl;
            

        }

        verifyBinary(buffer);
    }

    else{
        std::cout << "Error : File not open" << std::endl;
        return 1;
    }


    return 0;

}