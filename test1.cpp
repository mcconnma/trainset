#include <iostream>
#include <string>
#include <vector>
#include <exception>

using std::cout;
using std::endl;
using std::cerr;
using std::string;
using std::vector;
using std::exception;

int main(int argc, const char *argv[]) {

	string test("hello mark");

	test.erase(test.begin() + 2);

	cout << test << endl;

}

