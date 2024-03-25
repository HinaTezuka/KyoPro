#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

void print_element2(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int x : row) {
            cout << x << " ";
        }
        cout << endl;
    }
}

int main() {

    return 0;
}