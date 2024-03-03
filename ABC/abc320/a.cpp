#include <bits/stdc++.h>
using namespace std;

int main() {

    int a, b;
    cin >> a >> b;

    // int で指定してあげないとダメ？っぽい。あとで確認
    int ans = pow(a, b) + pow(b, a);

    cout << ans << "\n";

    return 0;
}