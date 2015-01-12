#include <algorithm>
#include <string>
#include <iostream>
#include <vector>

using namespace std;
 
int main()
{
	string s = "ccs";
	//vector<int> s = {2,1,1,1,1,2};
	sort(s.begin(), s.end());
	for (auto it = s.rbegin(); it != s.rend(); ++it) {
		cout << "perms of length: " << s.size() << endl;
		do {
			for (auto c : s) cout << c;
			cout <<  endl;
		} while (next_permutation(s.begin(), s.end()));
		s.pop_back();
	}
}
