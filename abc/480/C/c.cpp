#include <bits/stdc++.h>
#include <cmath>
using namespace std;
using ll = long long;


int main(){
    ll N,K,T;
    cin>>N>>K>>T;
    vector<ll> A(N, 0);
    for(int i=0;i<N;i++){
        cin >> A[i];
    }

    ll ans=0;
    ll last=T;
    // startを決める
    ll start=0;
    ll index=N-1;
    for(int i=N-1;i>=0;i--){
        // cout << "A[" << i << "]=" << A[i] << ", T=" << T << endl;
        if(A[i] <= T) {
            start=A[i];
            index=i;
            break;
        }
    }

    // cout << "start: " << start << endl;

    double value;
    for(int i=0;i<index+1;i++){
        // cout << "start: " << start << ", last: " << last << endl;
        value = double(last - (start + K)) / double(K);
        last=start;
        start=A[(index+1)-i-2];
        // cout << "start: " << start << ", last: " << last << ", value: " << value << ", ans: " << ans+ceil(value) << endl;
        if(value < 0) continue; 
        ans+=ceil(value);
        // cout << "ans: " << ans << endl;
    }

    // 最初だけ例外
    if(A[0] != 0){
        value = double(last)/double(K);
        if(value>0) ans+=ceil(value);
    }

    // cout << "start: " << start << ", last: " << last << ", value: " << value << ", ans: " << ans+ceil(value) << endl;

    cout << ans << endl;
    return 0;
}