#include <iostream>

using namespace std;
double F[51];
double Fib(int n){
	if(n<=1){
		return n;
	}
	if(F[n] != -1){
		return F[n];
	}
	F[n] = Fib(n-1) + Fib(n-2);
	return F[n];
}

int main(int argc, char** argv) {
	for(int i = 0; i<51; i++){
		F[i] = -1;
	}
	int n;
	cout<<"sayi giriniz ";
	cin>>n;
	double sonuc = Fib(n);
	cout<< sonuc;
	cout<< "\n";
	return 0; 
}
