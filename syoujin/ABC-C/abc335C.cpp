#include <iostream>
#include <deque>
#include <vector>

using namespace std;

// Function to update coordinates based on command
vector<int> command(char c, vector<int>& xy) {
    if (c == 'R') {
        xy[0] += 1;
    } else if (c == 'L') {
        xy[0] -= 1;
    } else if (c == 'U') {
        xy[1] += 1;
    } else if (c == 'D') {
        xy[1] -= 1;
    }
    return xy;
}

int main() {
    int n, q;
    cin >> n >> q;

    deque<vector<int>> Q;
    for (int i = 1; i <= n; ++i) {
        Q.push_back({i, 0});
    }

    for (int i = 0; i < q; ++i) {
        char x;
        string c;
        cin >> x >> c;
        if (x == '1') {
            vector<int> head = Q.front();
            vector<int> new_head = command(c[0], head);
            Q.push_front(new_head);
            Q.pop_back();
        } else {
            int index = stoi(c) - 1;
            cout << Q[index][0] << " " << Q[index][1] << endl;
        }
    }

    return 0;
}
