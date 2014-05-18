#include <iostream>
#include <list>
void subset_sum_recursive(std::list<int> numbers, int target, std::list<int> partial)
{
        int s = 0;
        for (std::list<int>::const_iterator cit = partial.begin(); cit != partial.end(); cit++)
        {
            s += *cit;
        }
        if(s == target)
        {
                std::cout << "sum([";

                for (std::list<int>::const_iterator cit = partial.begin(); cit != partial.end(); cit++)
                {
                    std::cout << *cit << ",";
                }
                std::cout << "])=" << target << std::endl;
        }
        if(s >= target)
            return;
        int n;
        for (std::list<int>::const_iterator ai = numbers.begin(); ai != numbers.end(); ai++)
        {
            n = *ai;
            std::list<int> remaining;
            for(std::list<int>::const_iterator aj = ai; aj != numbers.end(); aj++)
            {
                if(aj == ai)continue;
                remaining.push_back(*aj);
            }
            std::list<int> partial_rec=partial;
            partial_rec.push_back(n);
            subset_sum_recursive(remaining,target,partial_rec);

        }
}

void subset_sum(std::list<int> numbers,int target)
{
    subset_sum_recursive(numbers,target,std::list<int>());
}
int main()
{
    std::list<int> a;
    a.push_back (3); a.push_back (9); a.push_back (8);
    a.push_back (4);
    a.push_back (5);
    a.push_back (7);
    a.push_back (10);
    int n = 15;
    //std::cin >> n;
    subset_sum(a, n);
    return 0;
}
