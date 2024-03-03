#include <bits/stdc++.h>
using namespace std;

int main() {
    map<string, int> topcoders;
    topcoders["tourist"] = 3858;
    topcoders["ksun48"] = 3679;
    topcoders["Benq"] = 3658;
    topcoders["Um_nik"] = 3648;
    topcoders["apiad"] = 3638;
    topcoders["Stonefeang"] = 3630;
    topcoders["ecnerwala"] = 3613;
    topcoders["mnbvmar"] = 3555;
    topcoders["newbiedmy"] = 3516;
    topcoders["semiexp"] = 3481;

    string s;
    cin >> s;
    cout << topcoders[s] << endl;

    return 0;
}
