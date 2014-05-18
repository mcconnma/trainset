#include <iostream>
#include <queue>

void printsub(int* p, int len, std::queue<int> q) {

    if (!len) {
        while(!q.empty()) {
            std::cout << q.front() << " ";
            q.pop();
        }
        std::cout << "\n";
        return;
    }

    std::queue<int> t1(q);
    t1.push(p[0]);
    printsub(&(p[1]), len - 1, t1);

    std::queue<int> t2(q);
    printsub(&(p[1]), len - 1, t2);
}

int main() {
    int arr[] = {1, 1, 1, 1, 6, 6};                                     

    std::queue<int> q;
    printsub(arr, ((sizeof(arr))/(sizeof(arr[0]))), q);
}
