#include <algorithm>
#include <string>
#include <iostream>
 
int main()
{
		int count = 0;
    //std::string s = "ccccccccccccssss";
    std::string s = "ccc";
    std::sort(s.begin(), s.end());
    do {
        std::cout << s << '\n';
				++count;
    } while(std::next_permutation(s.begin(), s.end()));
		std::cout << "count: " << count << std::endl;
}
