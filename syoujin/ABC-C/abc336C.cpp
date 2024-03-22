#include <bits/stdc++.h>
using namespace std;

long long n;
// tuple<char, char, char, char, char> odds{'1', '3', '5', '7', '9'};

bool check(long long n) {
    string str_n = to_string(n);
    for(int i = 0; i < floor(str_n.size()/2); i++) {
        if (str_n[i] % 2 != 0){
            return false;
        }
        if (str_n[-i] % 2 != 0){
            return false;
        }
    }
    return true;
}

int main() {
    
    cin >> n;
    int cnt = 0;
    long long ans;

    if (n < 15625) {
        for(int i=0; i < 1000001; i+=2){
            if (cnt == n) {
                ans = i-1;
                break;
            }
            if (check(i)){
                cnt++;
            }
        }
    }
    else if (15625 < n && n < 1953125) {
        cnt = 15625;
        for(long long i=1000000; i < 1000000001; i+=2){
            if (cnt == n) {
                ans = i-1;
                break;
            }
            if (check(i)){
                cnt++;
            }
        }
    }
    else {
        for(long long i=1000000000; i < 1000000000001; i+=2){
            cnt = 1953125;
            if (cnt == n) {
                ans = i-1;
                break;
            }
            if (check(i)){
                cnt++;
            }
        }     
    }

    cout << ans << '\n';

    return 0;
}