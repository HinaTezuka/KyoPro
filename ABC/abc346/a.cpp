#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n, A[n+1];
    cin >> n;
    rep(i, n){
        int num;
        cin >> num;
        A[i] = num;
    }
    string ans;
    for(int i = 0; i < n-1; i++) ans += to_string(A[i]*(A[i+1])) + " ";
    cout << ans << '\n';
    
    return 0;
}