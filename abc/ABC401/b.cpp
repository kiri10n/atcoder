#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    int ans = 0;
    bool login = false;
    for(int i=0; i<n; i++){
        string s;
        cin >> s;
        if(s == "login") login = true;
        else if(s == "logout") login = false;
        else if(s == "private" && !login) ans++; 
    }

    cout << ans << endl;
    return 0;
}