// string::substr
#include <iostream>
#include <string>

void RecPermute(std::string soFar, std::string rest){
    if (rest.empty()) {
        std::cout << soFar << std::endl;
    } else {
        for (int i=0; i < rest.length(); i++) {
            std::string remaining = rest.substr(0,i) + rest.substr(i+1);
            RecPermute(soFar + rest[i], remaining);
        }
    }
}


int main ()
{
    std::string a1 = "Good";
    std::string a2 = "";
    RecPermute(a2, a1);
    return 0;
}