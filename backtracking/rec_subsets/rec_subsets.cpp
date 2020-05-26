// string::substr
#include <iostream>
#include <string>

void RecSubsets(std::string soFar, std::string rest){
    if (rest.empty()) {
        std::cout << soFar << std::endl;
    } else {
        //include the first char
        RecSubsets(soFar + rest[0], rest.substr(1));
        // exclude the first char
        RecSubsets(soFar, rest.substr(1));
    }
}


int main ()
{
    std::string a1 = "Good";
    std::string a2 = "";
    RecSubsets(a2, a1);
    return 0;
}