#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

void move(char command, string& current, int& h) {
    h--;
    if (command=='R') {
        int n = static_cast<int>(current[0]);
        n++;
        current[0] = static_cast<char>(n);
    }
    if (command=='L') {
        int n = static_cast<int>(current[0]);
        n--;
        current[0] = static_cast<char>(n);
    }
    if (command=='U') {
        int n = static_cast<int>(current[1]);
        n++;
        current[1] = static_cast<char>(n);
    }
    if (command=='D') {
        int n = static_cast<int>(current[1]);
        n--;
        current[1] = static_cast<char>(n);
    }
}

int main() {
    // 入力
    int n, m, h, k;
    cin >> n >> m >> h >> k;
    string S;
    cin >> S;
    // 回復アイテムがある座標
    map<string, int> kaifuku;
    rep(i, m) {
        string x, y;
        cin >> x >> y;
        string str_xy = x+y;
        if (kaifuku[str_xy] == 0) kaifuku[str_xy] = 1;
        else kaifuku[str_xy]++;
    }
    // 座標を初期化
    string current = "00";
    for(char s : S){
        move(s, current, h);
        if (h < 0) {
            cout << "No" << "\n"; 
            return 0;
        }
        if (kaifuku[current] > 0 && h < k){
            kaifuku[current]--;
            h = k;
        }
    }

    cout << "Yes" << "\n";

    return 0;
}