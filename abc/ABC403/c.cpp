#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;



int main(){
    ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m, q;
    cin >> n >> m >> q;
    vector<vector<int>> role(n);
    vector<bool> all_role(n);
    for(int i=0; i<q; i++){
        int query_type;
        cin >> query_type;
        if(query_type == 1){
            int x, y;
            cin >> x >> y;
            role[x-1].push_back(y-1);
        } else if(query_type == 2){
            int x;
            cin >> x;
            all_role[x-1] = true;
        } else if(query_type == 3){
            int x, y;
            cin >> x >> y;
            if(find(role[x-1].begin(), role[x-1].end(), y-1) != role[x-1].end()){
                cout << "Yes" << '\n';
            } else if(all_role[x-1]){
                cout << "Yes" << '\n';
            } else {
                cout << "No" << '\n';
            }
        }
    }
    return 0;
}