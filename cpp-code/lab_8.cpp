#include<bits/stdc++.h>
using namespace std;

int main(){

  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  int t;
  cin>>t;
  for(int i=0;i<t;i++){
  	int a,b;
  	cin>>a>>b;
  	if(a<b)swap(a,b);
  	cout<<a+b<<" ";
  	cout<<a-b<<" ";
  	cout<<a*b<<" ";
  	cout<<a/b<<endl;

  }

  return 0;
}
