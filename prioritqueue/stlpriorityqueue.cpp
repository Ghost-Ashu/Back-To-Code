#include<bits/stdc++.h>
using namespace std;

//max priority queue , mapheap 
// int main(){
//     priority_queue<int>pq;
//     pq.push(78);
//     pq.push(8);
//     pq.push(128);
//     pq.push(71);
//     pq.push(9);
//     pq.push(14);
//     cout<<pq.size()<<endl;
//     while(!pq.empty()){
//         cout<<pq.top()<<"   ";
//         pq.pop();
//     }
// }




//minheap queue , minheap

int main(){
    priority_queue<int,vector<int>,greater<int>>pq;
    pq.push(78);
    pq.push(8);
    pq.push(128);
    pq.push(71);
    pq.push(9);
    pq.push(14);
    cout<<pq.size()<<endl;
    while(!pq.empty()){
        cout<<pq.top()<<"   ";
        pq.pop();
    }
}
