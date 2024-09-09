#include<bits/stdc++.h>
using namespace std;

int main(){

	int n;
	cin>>n;

	long long x=1;

	// while(n){
	// 	x*=n;
	// 	n--;
	// }
	// cout<<x<<endl;


	for(int i=n;i>0;i--){
		x*=i;
	}
	cout<<x<<endl;

	return 0;
}