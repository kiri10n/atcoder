#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int N;
    string S;
    int ans=0;
    int renzoku=0;

    cin>>N;
    cin>>S;
    for(int i=0;i<N;i++){
        if(S[i]=='S') renzoku=0;
        else{
            renzoku++;
            if(ans<renzoku) ans=renzoku;
        }
    }

    cout << ans << endl;
    return 0;
}