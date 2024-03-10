#include <bits/stdc++.h>
using namespace std;

long long d;
int main() {
    cin >> d;
    long long ans = 1000000000000;
    for(int x=0; x < pow(10, 6); x++){
        int y = round(sqrt(d - pow(x, 2)));
        long long res = abs(pow(x, 2)+pow(y, 2)-d);
        ans = min(ans, res);
    }
    cout << ans << '\n';

    return 0;
}