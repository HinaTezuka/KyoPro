#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

int main() {
    int h, w;
    cin >> h >> w;
    vector<vector<int>> grid(h, vector<int>(w));
    pair<int, int> start;
    pair<int, int> goal;
    rep(i, h) {
        string s;
        cin >> s;
        rep(j, w){
            if (s[j] == 'S') start = make_pair(i, j);
            if (s[j] == 'T') goal = make_pair(i, j);
            grid[i][j] = s[j];
        }
    }
    int n;
    cin >> n;
    int r, c, e;
    vector<tuple<int, int, int>> kaifuku;
    bool flag = false;
    for(int i = 1; i < n+1; i++) {
        cin >> r >> c >> e;
        if ((start.first+1 == r && start.second == c) || (start.first == r && start.second+1 == c) || (start.first-1 == r && start.second == c) || (start.first == r && start.second-1 == c)){
            flag = true;
        }
        tuple<int, int, int> t = {r, c, e};
        kaifuku.push_back(t);
    }
    
    // start座標からいける座標に回復アイテムがなかったら終了
    if (!flag) {
        cout << "No" << "\n";
        return 0;
    }

    // bfs
    queue<int> Q;
    
    
    return 0;
}