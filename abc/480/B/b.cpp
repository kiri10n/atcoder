#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    int N,W;
    cin >>N>>W;

    vector<string> S(N);
    vector<int> ans(N, 0);

    for(int i=0;i<N;i++){
        cin>>S[i];
    }

    string T;
    int flag = 0;
    for(int i=0;i<W;i++){
        cin >> T;
        flag = 0;
        for(int j=0;j<N;j++){
            string s = S[j];
            if(T == s) {ans[j] += 1; flag=1; break;}
        }

        if(flag==0){
            int candidate = 0;
            int last_candidate = 0;
            for(int j=0;j<N;j++){
                string s = S[j];
                if(T.size() != s.size()) continue;
                // 何文字一致していないか
                int diff = 0;
                for(int k=0;k<T.size();k++){
                    if(T[k] != s[k]) diff += 1;
                }
                if(diff == 1) {
                    candidate += 1;
                    last_candidate = j;
                }
                // cout << "T:" << T << ",s:" <<s<< ",diff: " << diff << ",ans[j]" << ans[j] << endl;
            }
            if(candidate==1) ans[last_candidate] +=1;
            // cout << "candidate: " << candidate << endl;
        }

        for(int j=0;j<N;j++){
            // cout << "T:" << T << ",ans[" << j << "]=" << ans[j] << endl;
        }
    }

    for(int i=0;i<N;i++){
        cout << ans[i] << endl;
    }
    return 0;
}