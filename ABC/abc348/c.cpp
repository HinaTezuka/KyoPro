#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

int main() {
    int n;
    cin >> n;
    map<int, int> hmap;
    rep(i, n) {
        int a, c;
        cin >> a >> c;
        int keyToFind = c;
        auto it = hmap.find(keyToFind);
        if (it == hmap.end()){
            hmap[c] = a;
        }
        else {
            hmap[c] = min(hmap[c], a);
        }
    }

    // mapからvalueだけを取り出す
    vector<int> values;
    for (const auto &pair : hmap) {
        values.push_back(pair.second);
    }

    // 値をソートする
    sort(values.begin(), values.end());

    // 最小の要素を取得する
    int ans = values.back();

    cout << ans << "\n";

    return 0;
}