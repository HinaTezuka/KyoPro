#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

// 重み付きグラフの隣接リスト用
struct Edge {
    int to;
    int weight;
    Edge(int t, int w) : to(t), weight(w) { };
};

int main() {
    // 入力
    int n, m;
    cin >> n >> m;
    
    // 隣接リスト
    vector<vector<Edge>> G(n+1);
    for(int i = 0; i < m; i++){
        int from, to, weight;
        cin >> from >> to >> weight;
        G[from].push_back(Edge(to, weight));
        G[to].push_back(Edge(from, weight));
    }

    // 各街に対して BFS を行い、最大のコストを求める
    int ans = 0;
    for (int i = 1; i < n+1; i++){
        if(G[i].empty()) continue;
        int visited[19]; // 訪問済みの街かどうか
        for(int i = 1; i < n+1; i++) visited[i] = -1;
        queue<int> Q;
        Q.push(i);
        visited[i] += 1;
        // BFS
        vector<int> p;
        p.push_back(i);
        while(!Q.empty()){
            int pos = Q.front(); Q.pop();
            for(int j = 0; j < G[pos].size(); j++){
                int to = G[pos][j].to;
                if (visited[to] == -1){
                    visited[to] += 1;
                    Q.push(to);
                    p.push_back(to);
                }
            }
        }
        do{
            int tot = 0;
            for(int i = 0; i < p.size()-1; i++){
                if (G[p[i]].empty()) continue;
                for(int j = 0; j < G[p[i]].size(); j++){
                    if(G[p[i]][j].to == p[i+1]){
                        tot += G[p[i]][j].weight;
                        break;
                    }
                }
            }
            ans = max(ans, tot);
        } while (next_permutation(p.begin(), p.end()));
    }

    cout << ans << "\n";

    return 0;
}