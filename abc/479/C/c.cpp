#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int N, W;
    
    cin>>N;
    cin>>W;

    vector<vector<long long int>> a(N, vector<long long int>(2));
    long long int ans=0;

    for(int i=0;i<N;i++){
        cin >> a[i][0] >> a[i][1];
    }

    long long int N_sum, W_sum;
    for (int tmp = 0; tmp < (1 << N)+1; tmp++) {
        N_sum=0;
        W_sum=0;
        bitset<20> s(tmp);
        // (ビット列sに対する処理)
        for(int i=0;i<N;i++){
            if(s.test(i)){
                N_sum += a[i][0];
                W_sum += a[i][1];
            }
            
            if(W_sum>W){
                N_sum=0;
                break;
            }
            
        }
        // cout << N_sum << endl;
        // if(W_sum<=W){
        //     if(N_sum>ans) ans=N_sum;
        // }
        if(N_sum >ans) ans=N_sum;
    }

    

    cout << ans << endl;
    return 0;
}