#include<bits/stdc++.h>
using namespace std;
int main(){
	double a,b;
	cin>>a;
	char ch,pre;
	cin>>ch;
	cin>>b;
	cin>>pre;

	if(a<b)swap(a,b);
	if(pre=='='){
		if(ch=='+'){
			cout<<a<<"+"<<b<<" = "<<a+b<<endl;
		}
		else if(ch=='-'){
			cout<<a<<"-"<<b<<" = "<<a-b<<endl;
		}
		else if(ch=='*'){
			cout<<a<<"*"<<b<<" = "<<a*b<<endl;
		}
		else if(ch=='/'){
			cout<<a<<"/"<<b<<" = "<<a/b<<endl;
		}
		else{
			cout<<a<<"%"<<b<<" = "<<int(a)%int(b)<<endl;
		}
	}

}