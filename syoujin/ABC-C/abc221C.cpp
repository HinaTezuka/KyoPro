#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    cin >> n;

    string str_n = to_string(n);
    int k = str_n.size();
    int ans = 0;
    for(long long bit=0; bit < (1 << k); bit++) {
        string tmp = "";
        string tmp2 = "";
        for(int j=0; j < k; j++) {
            if (1 & (bit >> j)) {
                tmp += str_n[j];
            } else {
                tmp2 += str_n[j];
            }
        }
        if (tmp.size() > 1) sort(tmp.begin(), tmp.end(), greater<char>());
        else if (tmp.empty()) continue;
        if (tmp2.size() > 1) sort(tmp2.begin(), tmp2.end(), greater<char>());
        else if (tmp2.empty()) continue;

        ans = max(ans, stoi(tmp)*stoi(tmp2));
    }
    
    cout << ans << "\n";

    return 0;
}