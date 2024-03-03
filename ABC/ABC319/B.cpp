#include <bits/stdc++.h>
using namespace std;

int main() {

    int n;
    cin >> n;

    string ans;

    for(int i = 0; i < n+1; i++) {
        vector<int> pass;
        for(int j = 1; j <= 9; j++){
            if (n % j == 0 && i % (n/j) == 0) {
                pass.push_back(j);
            }       
        }
        if(!pass.empty()) {
            int min = *min_element(pass.begin(), pass.end());
            ans += to_string(min);
        } else {
            ans += "-";
        }
    }
    cout << ans << endl;

    return 0;
}