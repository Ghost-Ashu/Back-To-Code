#include<bits/stdc++.h>
using namespace std;

class priorityqueue{
    public:
    vector<int>pq;
    
    bool isempty(){
        return pq.size()==0;
    }
    int getmin(){
        if(isempty()){
            return 0;
        }
        return pq[0];
    }
    int  getsize(){
        return pq.size();
    }
    void insert(int x){
        pq.push_back(x);
        int child_index=pq.size()-1;
        while(child_index>0){
            int parent_index=(child_index-1)/2;

            if(pq[child_index]<pq[parent_index]){
                int temp=pq[child_index];
                pq[child_index]=pq[parent_index];
                pq[parent_index]=temp;
            }
            else{
                break;
            }
            child_index=parent_index;
        }   
    }
    int removemin(){
        if(isempty()){
            return 0;
        }
        int ans=pq[0];
        pq[0]=pq[pq.size()-1];
        pq.pop_back();
       
        //downheapify
        int parent_index=0;
        int leftchild_index=2*parent_index+1;
        int rightchild_index=2*parent_index+2;
        

        
        while(leftchild_index<pq.size()){
            int min_index=parent_index;


            if(pq[min_index]>pq[leftchild_index]){
                min_index=leftchild_index;
            }
            if(rightchild_index<pq.size() && pq[rightchild_index]<pq[min_index]){
                min_index=rightchild_index;
            }


            


            int temp=pq[min_index];
            pq[min_index]=pq[parent_index];
            pq[parent_index]=temp;
            parent_index=min_index;
            int leftchild_index=2*parent_index+1;
            int rightchild_index=2*parent_index+2;
            if(min_index==parent_index){
                break;
            }
            
        }
        return ans;
    }
   
};
int main(){
    priorityqueue p;
    p.insert(100);
    p.insert(10);
    p.insert(15);
    p.insert(4);
    p.insert(17);
    p.insert(21);
    p.insert(67);
    cout<<p.getsize()<<endl;
    while(!p.isempty()){
        cout<<p.removemin()<<" ";
    }
    cout<<endl;




}