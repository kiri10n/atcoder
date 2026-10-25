#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i=0; i<n; i++){
        cin >> a[i];
    }

    bool exist = false;
    for(int i=0; i<n-2; i++){
        if(a[i] == a[i+1] && a[i+1] == a[i+2]){
            exist = true;
            break;
        }
    }

    if(exist){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}