#include <iostream>
#include <vector>
#include <algorithm>

void print_subset( std::vector<bool> bit_mask, std::size_t req_size )
{
    if( std::count( bit_mask.begin(), bit_mask.end(), true ) == req_size )
    {
        static int cnt = 0 ;
        std::cout << ++cnt << ". [ " ;
        for( std::size_t i = 0 ; i < bit_mask.size() ; ++i )
            if( bit_mask[i] ) std::cout << i+1 << ' ' ;
        std::cout << "]\n" ;
    }
}

// generate the next Gray code (in reverse)
// http://en.wikipedia.org/wiki/Gray_code
bool next_bitmask( std::vector<bool>& bit_mask )
{
    std::size_t i = 0 ;
    for( ; ( i < bit_mask.size() ) && bit_mask[i] ; ++i )
        bit_mask[i] = false ;

    if( i < bit_mask.size() ) { bit_mask[i] = true ; return true ; }
    else return false ;
}

int main()
{
    std::size_t k, n ;
    std::cout << "n? " && std::cin >> n ;
    std::cout << "k? " && std::cin >> k ;
    std::vector<bool> bit_mask(n) ;
    do print_subset( bit_mask, k ) ; while( next_bitmask(bit_mask) ) ;
}
