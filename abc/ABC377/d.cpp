#include <iostream>
#include <set>
#include <utility>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    set<pair<int, int>> ans_set;

    // 各区間 (l_i, r_i) を入力し、条件を満たす区間を ans_set に追加
    for (int i = 0; i < n; ++i) {
        int l_i, r_i;
        cin >> l_i >> r_i;

        for (int l = 1; l <= l_i; ++l) {
            for (int r = r_i; r <= m; ++r) {
                ans_set.insert(make_pair(l, r));
            }
        }
    }

    // 全ての区間の組み合わせの数を計算
    int all_combinations = (m * (m + 1)) / 2;

    // 含まれない区間の数を出力
    cout << all_combinations - ans_set.size() << endl;

    return 0;
}
