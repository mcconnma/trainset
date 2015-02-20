
#include <iostream>
#include <vector>
#include <deque>
#include <list>
#include <algorithm>
#include <exception>

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

}
