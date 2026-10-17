#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    char S11, S12, S21, S22;
    cin >> S11 >> S12;
    cin >> S21 >> S22;

    string ans = "No";
    if(S11 == 'A'){
        if(S12 == 'D' || S21 == 'D') ans="Yes";
    }
    if(S12=='A'){
        if(S11=='D'||S22=='D') ans="Yes";
    }
    if(S21=='A'){
        if(S11=='D'||S22=='D') ans="Yes";
    }
    if(S22=='A'){
        if(S12=='D'||S21=='D') ans="Yes";
    }

    cout << ans << endl;
    return 0;
}