#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

char buf[16];
std::vector<char> v = {'G', 'R', 'I', 'S', 'A'};

void lose() {
    puts("Bye!");
    exit(1);
}

void win() {
    system("/bin/sh");
    exit(0);
}

int main() {
    char ductf[6] = "DUCTF";
    char* d = ductf;

    std::cin >> buf;
    std::cout << buf << std::endl;
    std::cout << v.size() << std::endl;
    if(v.size() == 5) {
        for(auto &c : v) {
            if(c != *d++) {
                std::cout << "inner\n";
                lose();
            }
        }

        win();
    }

    std::cout << "outer\n";
    lose();
}
