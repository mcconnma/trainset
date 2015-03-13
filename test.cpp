
#include <iostream>
#include <vector>
#include <deque>
#include <list>
#include <algorithm>
#include <exception>
#include <cstdlib>
#include <cstdio>

using std::cout;
using std::endl;
using std::vector;
using std::deque;
using std::list;
using std::string;
using std::count;
using std::exception;

class Base {

protected:

public:
	int getIt() { return it; }	
	Base() : it(5) {}
	int it;

};

class Derived : public Base {

};

class TestException : public exception {

};

void print_ip(int ip)
{
    unsigned char bytes[4];
    bytes[0] = ip & 0xFF;
    bytes[1] = (ip >> 8) & 0xFF;
    bytes[2] = (ip >> 16) & 0xFF;
    bytes[3] = (ip >> 24) & 0xFF;	
    printf("%d.%d.%d.%d\n", bytes[3], bytes[2], bytes[1], bytes[0]);        
}

class Test {

public:

	Test() {}
	Test(string name) { s = name; }
	~Test() {}

	string getName() { return s; }
	string setName(string name) { s = name; }

private:
	int i;
	string s;

};

void testarray() {
	
	int SIZE = 2;

	string t[] = { "hello", "mark" };

	for (int i = 0; i < SIZE; i++) {
		cout << t[i] << endl;
	}

}


string reverseit(string& in) {
	string out;
	string::reverse_iterator si;
	for (si = in.rbegin(); si != in.rend(); si++) {
		out.push_back(*si);
	}
	return out;
}

int main(int argc, char **argv) {

	cout << "main" << endl;

	try {
		throw TestException();
	}
	catch (const exception &e) {
		cout << "e: " << e.what() << endl;
	}

	vector<string> temp;
	vector<string>::reverse_iterator i;

	temp.push_back("hello");
	temp.push_back("mark");

	for (i = temp.rbegin(); i != temp.rend(); i++) {
		cout << *i << endl;
	}

	deque<string> d;
	deque<string>::reverse_iterator di;

	d.push_back("hello");
	d.push_back("mark");

	for (di = d.rbegin(); di != d.rend(); di++) {
		cout << *di << endl;
	}

	list<Test> l;
	list<Test>::iterator li;

	Test mark("mark");
	Test adri("adri");
	l.push_back(mark);
	l.push_back(adri);

	for (li = l.begin(); li != l.end(); li++) {
		cout << li-> getName() << endl;
	}

	string s("mark");
	int c = count(d.begin(), d.end(), "adri");
	cout << "adri count: " << c << endl;

	cout << "reverseit: " << reverseit(s) << endl;
	Derived D;
	cout << "getit: " << D.getIt() << endl;

	testarray();

	print_ip(1249295239);

}
