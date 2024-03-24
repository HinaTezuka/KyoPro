#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

// int A[100009];

int main() {
    // 入力
    unsigned int n;
    cin >> n;
    int num;
    vector<unsigned int> A(n);
    rep(i, n) {
        cin >> num;
        A[i] = num;
    }

    vector<unsigned int> A2 = A;
    // 優先度付きキューで最大値、最小値を管理
    priority_queue<unsigned int> bigger(A.begin(), A.end());
    priority_queue<unsigned int, vector<unsigned int>, greater<unsigned int>> smaller(A2.begin(), A2.end());
    
    int mx = bigger.top();
    bigger.pop();
    int mn = smaller.top();
    
    
    

    return 0;
}