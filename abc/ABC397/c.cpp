#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> a(n);

    vector<int> num_kind_forward(n);
    vector<int> num_kind_backward(n);
    set<int> left;
    for(int i=0; i<n; i++){
        cin >> a[i];
        left.insert(a[i]);
        num_kind_forward[i] = left.size();
    }

    set<int> right;
    for(int i=0; i<n; i++){
        right.insert(a[n-1-i]);
        num_kind_backward[i] = right.size();
    }

    // cout << "num_kind_forward: ";
    // for(auto x: num_kind_forward){
    //     cout << x << " ";
    // }
    // cout << endl;
    // cout << "num_kind_backward: ";
    // for(auto x: num_kind_backward){
    //     cout << x << " ";
    // }
    // cout << endl;

    int ans = 0;
    for(int i=0; i<n-1; i++){
        int addition = num_kind_forward[i] + num_kind_backward[n-i-2];
        ans = max(ans, addition);
    }

    cout << ans << endl;

    return 0;
}

// 全部で6種類
// 1 2 3 3 3 4 5 6 6 6
// 6 6 6 5 4 3 3 3 2 1


// 1 2 3 3 4 4 5 6 6 6