#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

vector<int> graph[100009];

int main(){
    int n, m;
    cin >> n >> m;

    int ans = 0;
    for(int i=0; i<m; i++){
        int u, v;
        cin >> u >> v;
        if(u == v) {
            ans++;
        }else{
            for(auto x: graph[u]){
                if(x == v){
                    ans++;
                }
            }
            for(auto x: graph[v]){
                if(x == u){
                    ans++;
                }
            }
        }
        graph[u].push_back(v);
    }

    cout << ans << endl;
    return 0;
}