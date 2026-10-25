#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int main(){
    int n, d;
    cin >> n >> d;
    vector<int> a(n);
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    int prev = a[0];
    int num_continuous_d = 0;
    int ans = 0;
    for(int i=1; i<n; i++){
        if(a[i] - prev == d){
            num_continuous_d++;
        } else if(a[i] - prev > d){
            // 1->1, 2->1, 3->2, 4->2, 5->3, 6->3
            ans += ceil(num_continuous_d / 2.0f);
            num_continuous_d = 0;
        }
        prev = a[i];
    }
    cout << num_continuous_d << endl;
    ans += ceil(num_continuous_d / 2.0f);
    cout << ans << endl;
    
    return 0;
}