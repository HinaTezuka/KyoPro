#include <bits/stdc++.h>
#include <numeric>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void print_element(int x) { // for_each(vec.begin(), vec.end(), print_element);
    cout << x << " ";
}

// void print_element2(const vector<vector<int>>& matrix) {
//     for (const auto& row : matrix) {
//         for (int x : row) {
//             cout << x << " ";
//         }
//         cout << endl;
//     }
// }

int main() {
    // int A[9][9];
    vector<vector<int> > A(9, vector<int>(9));
    rep(i, 9){
        rep(j, 9){
            cin >> A[i][j];
        }
    }
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            cout << A[i][j] << "\n";
        }
    }
    // rep(i, 9){
    //     int tot = reduce(A[i].begin(), A[i].end());
    //     if (tot != 45) {
    //         cout << 'No' << "\n";
    //         exit(0);
    //     }
    // }
    return 0;
}