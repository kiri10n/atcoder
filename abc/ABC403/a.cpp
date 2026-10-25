#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    int ans = 0;
    for(int i=0; i<n; i++){
        int a_i;
        cin >> a_i;
        if(i%2==0) ans += a_i;
    }
    cout << ans << endl;
    return 0;
}