#include <iostream>
#include <vector>

using namespace std;

// // 指定した部分行列を右に90度回転させる関数
// void rotate90(vector<vector<char>> &a, int start, int end) {
//     int size = end - start;
//     for (int layer = 0; layer < size / 2; ++layer) {
//         int first = start + layer;
//         int last = end - layer - 1;
//         for (int i = first; i < last; ++i) {
//             int j = last - i + first;
//             char tmp = a[first][i]; // 上側を保存

//             // 左 -> 上
//             a[first][i] = a[j][first];

//             // 下 -> 左
//             a[j][first] = a[last][j];

//             // 右 -> 下
//             a[last][j] = a[i][last];

//             // 上 -> 右
//             a[i][last] = tmp;
//         }
//     }
// }

// 指定した部分行列を右に90度回転させる関数
void rotate90(vector<vector<char>> &a, int start, int end) {
    int first = start;
    int last = end - 1;
    for (int i = first; i < last; ++i) {
        int j = last - i + first;
        char tmp = a[first][i]; // 上側を保存

        // 左 -> 上
        a[first][i] = a[j][first];

        // 下 -> 左
        a[j][first] = a[last][j];

        // 右 -> 下
        a[last][j] = a[i][last];

        // 上 -> 右
        a[i][last] = tmp;
    }
}

int main() {
    int n;
    cin >> n;

    // 文字列を2次元ベクトルに変換
    vector<vector<char>> a(n, vector<char>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> a[i][j];
        }
    }

    // 範囲ごとに90度右回転
    for (int i = 0; i < n / 2; ++i) {
        if (i % 4 == 0){
            rotate90(a, i, n - i);
        }
        else if (i % 4 == 1) {
            rotate90(a, i, n - i);
            rotate90(a, i, n - i);
        }
        else if (i % 4 == 2) {
            rotate90(a, i, n - i);
            rotate90(a, i, n - i);
            rotate90(a, i, n - i);
        }
    }

    // 結果の行列を出力
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << a[i][j];
        }
        cout << endl;
    }

    return 0;
}