// find all the permutations of a string
// using Knuth radnom shuffling algorithm!

#include <iostream>
#include <string>

template <typename T, class Func>
void permutation(T array, std::size_t N, Func func)
{
    func(array);
    for (std::size_t n = N-1; n > 0; --n)
    {
        for (std::size_t k = 0; k <= n; ++k)
        {
            if (array[k] == array[n]) continue;
            using std::swap;
            swap(array[k], array[n]);
            func(array);
        }
    }
}

int main()
{
    while (std::cin.good())
    {
        std::string str;
        std::cin >> str;
        permutation(str, str.length(), [](std::string const &s){ 
            std::cout << s << std::endl; });
    }
}
