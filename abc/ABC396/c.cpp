#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n, m;
    cin >> n >> m;

    vector<int> b(n);
    for(int i=0; i<n; i++){
        cin >> b[i];
    }

    vector<int> w(m);
    for(int i=0; i<m; i++){
        cin >> w[i];
    }

    // ソート
    sort(b.begin(), b.end(), greater<int>());
    sort(w.begin(), w.end(), greater<int>());

    // bの累積和
    vector<int> b_sum(n);
    b_sum[0] = b[0];
    for(int i=1; i<n; i++){
        b_sum[i] = b_sum[i-1] + b[i];
    }

    int b_max_sum_index = distance(b_sum.begin(), max_element(b_sum.begin(), b_sum.end()));

    // wの累積和
    vector<int> w_sum(m);
    w_sum[0] = w[0];
    for(int i=1; i<m; i++){
        w_sum[i] = w_sum[i-1] + w[i];
    }  

    int w_max_sum_index = distance(w_sum.begin(), max_element(w_sum.begin(), w_sum.end()));

    // cout << "b_sum: ";
    // for(auto x: b_sum){
    //     cout << x << " ";
    // }
    // cout << endl;
    
    // cout << "w_sum: ";
    // for(auto x: w_sum){
    //     cout << x << " ";
    // }
    // cout << endl;

    // if(b_max_sum_index >= w_max_sum_index){
    //     cout << b_sum[b_max_sum_index] + w_sum[w_max_sum_index] << endl;
    //     return 0;
    // }

    int ans = max(0, b_sum[0]);
    // for(int num_w=b_max_sum_index+1; num_w<min(w_max_sum_index+1, n); num_w++){
    //     ans = max(ans, *max_element(b_sum.begin()+num_w-1, b_sum.end()) + w_sum[num_w-1]);
    // }
    for(int num_b=1; num_b<=n; num_b++){
        ans = max(ans, b_sum[num_b-1] + *max_element(w_sum.begin(), min(w_sum.begin()+num_b, w_sum.end())));
    }

    cout << ans << endl;
    return 0;
}