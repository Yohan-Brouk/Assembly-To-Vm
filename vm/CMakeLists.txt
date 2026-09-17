# Version minimale de CMake requise
cmake_minimum_required(VERSION 3.10)

# Nom du projet
project(VirtualMachine CXX)

# Standard C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Mode Release par défaut (-O3 pour les performances)
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

# Déclaration de l'exécutable 'vm'
add_executable(vm
    src/main.cpp
    src/loader.cpp
    src/vm.cpp
)

# Inclusions (indique à CMake de chercher les fichiers .hpp / .h dans src/)
target_include_directories(vm PRIVATE src)