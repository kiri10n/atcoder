#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(){
    string s;
    cin >> s;

    int ans = 0;

    for(size_t interval = 1; interval <= s.size()/2; interval++){
        size_t i, j, k;
        for(i=0; i<s.size(); i++){
            j = i + interval;
            k = j + interval;
            if (k >= s.size()) break;

            if(s[i] == 'A' && s[j] == 'B' && s[k] == 'C'){
                ans++;
            }
        }
    }

    cout << ans << endl;
    return 0;
}