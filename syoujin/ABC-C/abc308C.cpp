#include <iostream>
#include <vector>
#include <map>
#include <iomanip>

using namespace std;

long double culc_rate(int a, int b) {
    return static_cast<long double>(a) / (a + b);
}

int main() {
    int n;
    cin >> n;

    map<long double, vector<int>> res;

    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        long double score = culc_rate(a, b);
        res[score].push_back(i + 1);
    }

    map<long double, vector<int>, greater<long double>> sorted_res(res.begin(), res.end());

    for (const auto& item : sorted_res) {
        for (int val : item.second) {
            cout << val << " ";
        }
    }
    cout << endl;

    return 0;
}
