#include <bits/stdc++.h>
using namespace std;
int n, W, w[100009], v[109];
long long dp[109][100009];

int main() {
    cin >> n, W;
    for (int i = 1; i < n+1; i++) {
        cin >> w[i], v[i];
    }
    // 2次元DP
    for(int i = 0; i < n+1; i++) {
        for (int j = 0; j < W; j++) {
            dp[i][j] = -1500000000000LL;
        }
    }

    dp[0][0] = 0;
    for (int i = 1; i < n+1; i++) {
        for (int j = 0; j < W; j++) {
            if (j < w[i]) {
                dp[i][j] = dp[i-1][j];
            }else{
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i]);
            }
        }
    }
    long long ans = 0;
    for (int i = 1; i < W; i++) {
        ans = max(ans, dp[n][i]);
    }
    cout << ans << endl;
    
    return 0;
}