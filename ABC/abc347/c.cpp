#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

int main() {
    // 入力
    int n, a, b;
    cin >> n >> a >> b;
    vector<int> d(n+1);
    for(int i = 1; i < n+1; i++) cin >> d[i];

    int tot = a + b;
    bool f = true;
    for (int i = 1; i < n+1; i++){
        if(d[i] <= a) continue;
        if(d[i] % tot > a) f = false;
    }
    if (f) cout << "Yes" << "\n";
    else cout << "No" << "\n";

    return 0;
};