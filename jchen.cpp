#include <iostream>
#include <set>
#include <queue>
#include <iterator>

using namespace std;

template<typename T> void copy_set(set<T> &ds, set<T> &ss)
{
    typename set<T>::iterator it;
    for(it = ss.begin(); it != ss.end(); ++it){
        ds.insert(*it);
    }
}

template<typename T> void print_set(set<T> &s)
{
    copy(s.begin(), s.end(), ostream_iterator<T>(cout, "  "));
    cout << endl;
}

template<typename T> void list_subset(set<T> &ss, set<T> &sr)
{
    if(sr.empty() && ss.empty()){
        return;
    }

    if(sr.empty()){
        print_set(ss);
        return;
    }
    else{
        typename set<T>::iterator it = sr.begin();
        T a = *it;

        set<T> t1, t2, t3, t4;
        copy_set(t1, ss);
        copy_set(t3, sr);
        t1.insert(a);
        t3.erase(a);
        list_subset(t1, t3);

        copy_set(t2, ss);
        copy_set(t4, sr);
        t4.erase(a);

        list_subset(t2, t4);
    }
}

int main(int argc, char* argv[])
{
    set<char> s,ss;

    s.insert('1');
    s.insert('1');
    s.insert('1');
    s.insert('2');

    list_subset(ss, s);

    return 0;
}
