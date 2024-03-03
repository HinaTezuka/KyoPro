#include <bits/stdc++.h>
using namespace std;

int main() {

    string s;
    cin >> s;
    int len_s = s.size();

    int count = 0;
    for(int i = 0; i < len_s; i++) {
        for(int j = 0; j < len_s; j++){
            if(s[i] == s[j]) {
                count++;
            }
        }
    }

    cout << count << "\n";

    return 0;
}