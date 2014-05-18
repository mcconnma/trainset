#include <string>
#include <iostream>

template<typename Consume>
void permutations(std::string s, Consume consume, std::size_t start = 0) {
    if (start == s.length()) consume(s);
    for (std::size_t i = start; i < s.length(); i++) {
        std::swap(s[start], s[i]);
        permutations(s, consume, start + 1);
    }
}

int main(void) {
    std::string s = "abcd";
    permutations(s, [](std::string s) {
        std::cout << s << std::endl;
    });
}
