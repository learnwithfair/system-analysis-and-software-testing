#include<bits/stdc++.h>
using namespace std;
int main(){

	int n;
	cin>>n;

	vector<double>vec(2*n);

	for(int i=0;i<2*n;i++){
		cin>>vec[i];
	}

	char ch;
	cin>>ch;

	sort(vec.begin(),vec.end());

	if(ch=='+'){
		for(int i=0;i<2*n;i+=2){
			cout<<vec[i]<<"+"<<vec[i+1]<<"="<<vec[i]+vec[i+1]<<endl;
		}
	}
	else if(ch=='-'){
		for(int i=0;i<2*n;i+=2){
			cout<<vec[i]<<"-"<<vec[i+1]<<"="<<abs(vec[i]-vec[i+1])<<endl;
		}
	}
	else if(ch=='*'){
		for(int i=0;i<2*n;i+=2){
			cout<<vec[i]<<"*"<<vec[i+1]<<"="<<vec[i]*vec[i+1]<<endl;
		}
	}
	else if(ch=='/'){
		for(int i=0;i<2*n;i+=2){
			cout<<vec[i]<<"/"<<vec[i+1]<<"="<<vec[i]/vec[i+1]<<endl;
		}
	}
	else{
		for(int i=0;i<2*n;i+=2){
			cout<<vec[i]<<"%"<<vec[i+1]<<"="<<int(vec[i])%int(vec[i+1])<<endl;
		}
	}


}