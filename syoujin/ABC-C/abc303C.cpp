#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

void move(char command, vector<int>& current, int h) {
    h--;
    if (command=='R') current[0] += 1;
    if (command=='L') current[0] -= 1;
    if (command=='U') current[1] += 1;
    if (command=='D') current[1] -= 1;
}

int main() {
    // 入力
    int n, m, h, k;
    cin >> n >> m >> h >> k;
    string S;
    cin >> S;
    // 回復アイテムがある座標
    vector<vector<int> > kaifuku(m, vector<int>(2));
    rep(i, m) {
        int x, y;
        cin >> x >> y;
        kaifuku[i] = {x, y};
    }
    // 座標を初期化
    vector<int> current = {0, 0};
    for(char s : S){
        move(s, current, h);
        if (h < 0) {
            cout << "No" << "\n"; 
            return 0;
        }
        auto it = find(kaifuku.begin(), kaifuku.end(), current);
        if (it != kaifuku.end() && h < k){
            h = k;
            int idx = distance(kaifuku.begin(), it);
            kaifuku.erase(kaifuku.begin()+idx);
        }
    }

    cout << "Yes" << "\n";

    return 0;
}