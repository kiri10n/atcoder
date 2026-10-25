#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    string t, u;
    cin >> t >> u;
    for(int i=0; i<t.size()-u.size()+1; i++){
        int match=0;
        for(int j=0; j<u.size(); j++){
            if(t[i+j] == u[j] || t[i+j] == '?') match++;
            else break;
        }
        if(match == u.size()){
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}