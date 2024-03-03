#include <bits/stdc++.h>
using namespace std;

int main() {

    int m;
    cin >> m;
    vector<string> slots(3);
    for(int i = 0; i < 3; i++){
        cin >> slots[i];
    }
    vector<int> time;

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < m;j++) {
            for(int k = 0; k<m; k++) {
                if (slots[i] == slots[j] || slots[j] == slots[k]){
                    
                }
            }
        }
    }

    return 0;
}