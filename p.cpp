#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>
using namespace std;

size_t factorial( size_t n )
  {
  size_t result = 1;
  while (n > 1)
    result *= n--;
  return result;
  }

template <typename Iterator>
bool next_take_r( size_t r, Iterator begin, Iterator end )
  {
  bool result = false;
  size_t n = factorial( distance( begin, end ) - r );
  for (size_t x = 0; x < n; x++)
    result = next_permutation( begin, end );
  return result;
  }

int main()
  {
  //vector <int> ns { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
  vector <int> ns { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  2, 2 };
  //vector <int> ns { 'c', 'c', 'c', 'c', 's', 's' };

  size_t n = 8;
  
  do {
    copy_n( ns.begin(), min( n, ns.size() ), ostream_iterator <int> ( cout, " " ) );
    cout << "\n";
    }
  while (next_take_r( n, ns.begin(), ns.end() ));

  return 0;
  }
