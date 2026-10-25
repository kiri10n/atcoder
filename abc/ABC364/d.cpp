#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    vector<int> ans;
    for (int i = 0; i < q; i++) {
        int b, k;
        cin >> b >> k;
        vector<int> dist(n);
        for (int j = 0; j < n; j++) {
            dist[j] = abs(a[j] - b);
        }
        sort(dist.begin(), dist.end());
        ans.push_back(dist[k - 1]);
    }

    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << endl;
    }

    return 0;
}