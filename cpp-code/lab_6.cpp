#include<bits/stdc++.h>
using namespace std;

void sum(vector<int>vec1){

	int sm=0,i=0;
	do{
		sm+=vec1[i];
		i++;
	}
	while(i<vec1.size());

	cout<<sm<<endl;
}

void avg(vector<int>vec1){

	int sm=0,i=0;
	do{
		sm+=vec1[i];
		i++;
	}
	while(i<vec1.size());
	cout<<(sm)/vec1.size()<<endl;
}

int  main(){
	int n;
	cin>>n;

	vector<int>vec(n);
	for(int i=0;i<n;i++){
		cin>>vec[i];
	}

	sum(vec);
	avg(vec);

	return 0;

}