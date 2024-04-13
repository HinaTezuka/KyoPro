#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

int r, c, sy, sx, gy, gx;
// 各座標のcharとその座標(x, y)e
vector<tuple<char, int, int>> grid(r);

int main() {
    // 入力
    cin >> r >> c;
    cin >> sy >> sx;
    cin >> gy >> gx;
    pair<int, int> start = make_pair(sx, sy);
    pair<int, int> goal = make_pair(gx, gy);
    
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            char s;
            cin >> s;
            grid.push_back({s, i, j});
        }
    }

    // 連接行列
    vector<vector<tuple<char, int, int>>> G(r);

    // bfs
    queue<int> Q;
    Q.push(1);
    while(!Q.empty()){
        int pos = Q.front();
        Q.pop();
        for(int i = 0; i < )
    }
    
    return 0;
}