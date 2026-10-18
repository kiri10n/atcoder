#include <bits/stdc++.h>
#include <cmath>
using namespace std;
using ll = long long;


int main(){
    ll N,K,T;
    cin>>N>>K>>T;
    vector<ll> A(N, 0);
    for(ll i=0;i<N;i++){
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    ll ans=0;
    ll tail=0; // ここまではカウント済み
    for(ll i=0;i<N;i++){
        if(tail > T) break;

        if(A[i] > T) break;

        if(tail > A[i]){
            tail = A[i] + K;
            continue;
        }

        ans += ceil(double(A[i] - tail) / double(K));
        tail = A[i] + K;
    }

    if(T > tail) ans += ceil(double(T - tail) / double(K));

    cout << ans << endl;
    return 0;
}