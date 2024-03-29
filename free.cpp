#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

int a[19], b[19], c[19];
vector<int> G[19];

int main() {
    // 入力
    int n, m;
    cin >> n >> m;
    for(int i = 1; i < m+1; i++) cin >> a[i] >> b[i] >> c[i];
    // 連結行列
    for(int i = 1; i < m+1; i++){
        G[a[i]].push_back(b[i]);
        G[b[i]].push_back(a[i]);
    }

    // 各町にたいして有効pathを求める
    int ans = -1;
    for (int i = 1; i < n+1; i++){
        queue<int> Q;
        Q.push(i);
        int dist[n+1];
        for(int i = 1; i < n+1; i++) dist[i] = -1;
        dist[i] = 0;
        int tot = 0; // 合計コスト
        // bfs
        while(!Q.empty()){
            int pos = Q.front(); Q.pop();
            tot += c[pos];
            for(int j = 0; j < G[pos].size(); j++){
                int to = G[pos][j];
                if (dist[to] == -1){
                    dist[to] = dist[pos]+1;
                    Q.push(to);
                }
            }
        }
        ans = max(ans, tot);
    }

    cout << ans << "\n";

    return 0;
}