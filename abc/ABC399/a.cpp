#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    string s, t;
    cin >> s >> t;

    int ans = 0;
    for(int i=0; i<n; i++){
        if(s[i] != t[i]) ans++;
    }

    cout << ans << endl;
    return 0;
}