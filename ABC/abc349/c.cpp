#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

string encode(const string& str) {
    int n = (int)str.size();
    string ret = ""; // 答えを格納
    for (int l = 0; l < n;) {
        int r = l + 1;
        for (; r < n && str[l] == str[r]; r++) {};
        ret.push_back(str[l]);
        string num_str = to_string(r - l); // 出現回数
        ret += num_str;
        l = r;
    }
    return ret;
}

// bool check(string s, string T){
    
// }

int main() {
    string S, T;
    cin >> S;
    cin >> T;
    // ランレングス圧縮
    // string s = encode(S);

    map<char, vector<int>> hmap;
    for(int i = 0; i < S.length(); i++){
        auto it = find(S.begin(), S.end(), )
    }
    
    return 0;
}