#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    if(m == 0){
        cout << 0 << endl;
        return 0;
    }
    vector<vector<int>> graph(n, vector<int>());
    for(int i=0; i<m; i++){
        int u, v;
        cin >> u >> v;
        u--; v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<bool> visited(n);
    int s = 0; // 連結成分の数
    for(int i=0; i<n; i++){
        if(!visited[i]){
            s++;
            queue<int> q;
            q.push(i);
            while(!q.empty()){
                int x = q.front();
                q.pop();
                for(auto v: graph[x]){
                    if(!visited[v]){
                        visited[v] = true;
                        q.push(v);
                    }
                }
            }
        }
    }

    cout << m - n + s << endl;

    return 0;
}