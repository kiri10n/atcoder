#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    string s;
    cin >> s;

    // bool is_i = true;
    // int ans = 0;

    // if(s[0] == 'o'){
    //     s = 'i' + s;
    //     ans++;
    // }



    // for(char c: s){
    //     if(c == 'i'){
    //         if(!is_i) ans++;
    //     }else{
    //         if(is_i) ans++;
    //     }
    //     is_i = !is_i;
    // }

    // if(!is_i) ans++;

    // cout << ans << endl;

    // int ans = 0;
    int num_io = 0;
    char prev = s[0];
    for(char c: s){
        if(prev == 'i' && c == 'o'){
            num_io++;
        }
        prev = c;
    }
    
    cout << s.size() - num_io * 2 << endl;

    return 0;
}