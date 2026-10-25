#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    int ans;

    vector<int> a(n+1, 1);

    a[k] = k;

    for(int i=k; i<n; i++){
        a[i+1] = (2 * a[i] - a[i-k]) % 1000000000;
    }

    cout << a[n] << endl;
    return 0;
}