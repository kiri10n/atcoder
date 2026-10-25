#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> p(n);
    vector<int> rank(n);
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        p[i] = x;
    }

    int r=1;
    int rest = n;
    while(rest > 0){
        int max = *max_element(p.begin(), p.end());
        int k =0;
        for(int j=0; j<n; j++){
            if(p[j] == max){
                rank[j] = r;
                p[j] = 0;
                rest--;
                k++;
            }
        }
        r += k;
    }

    for(int i=0; i<n; i++){
        cout << rank[i] << endl;
    }
    return 0;
}