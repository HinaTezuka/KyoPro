/* 問題：https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_C&lang=jp */

#include <iostream>
#include <vector>
using namespace std;

int main() {
    /* 入力受け取り */
    int n, Q;
    cin >> n >> Q;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    /* Q 回分のクエリを処理 */
    for (int j = 0; j < Q; ++j) {
        long long x; cin >> x; // 各クエリ x

        /* 合計値 */
        long long res = 0;

        /* 区間の左端 left で場合分け */
        for (int left = 0; left < n; ++left) {
            long long sum = 0;
            int right = left; // [left, right) の総和が x 以下となる最大の right を求める

            /* sum に a[right] を加えても大丈夫なら right を動かす */
            while (right < n && sum + a[right] <= x) {
                sum += a[right];
                ++right;
            }

            /* break した状態で right は条件を満たす最大 */
            res += (right - left);
        }

        cout << res << endl;
    }
}
