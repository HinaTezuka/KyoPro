#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

void move(char command, pair<int, int>& current, int& h) {
    h--;
    if (command=='R') {
        current.first++;
    }
    if (command=='L') {
        current.first--;
    }
    if (command=='U') {
        current.second++;
    }
    if (command=='D') {
        current.second--;
    }
}

int main() {
    // 入力
    int n, m, h, k;
    cin >> n >> m >> h >> k;
    string S;
    cin >> S;
    // 回復アイテムがある座標とその座標にある回復アイテムの数
    map<pair<int, int>, int> kaifuku;
    rep(i, m) {
        int x, y;
        cin >> x >> y;
        pair<int, int> p(x, y);
        if (kaifuku[p] == 0) kaifuku[p] = 1;
        else kaifuku[p]++;
    }
    // 座標を初期化
    pair<int, int> current (0, 0);
    for(char s : S){
        move(s, current, h);
        if (h < 0) {
            cout << "No" << "\n"; 
            return 0;
        }
        if (h < k && kaifuku[current] > 0){
            kaifuku[current]--;
            h = k;
        }
    }

    cout << "Yes" << "\n";

    return 0;
}