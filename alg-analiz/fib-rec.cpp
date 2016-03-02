#include <iostream>

using namespace std;


//recursive fib = 2^N
int fib(int n){
    if(n<=1)
	    return 1;
    else
	    return fib(n-1)+fib(n-2);
}

//

//fib = N
int fibbonacci(int n){
    if(n<=1)
	    return 1;

    int last = 1;
    int nextToLast = 1;
    int answer = 1;

    for(int i = 2; i<=n; i++){
	answer = last + nextToLast;
	nextToLast = last;
	last = answer;
    
    }
    return answer;
}

//
// ortalama fonksiyonu N=1

int ortalama(int a, int b, int c){

	return (a+b+c)/3;

}


int main (){
    cout << fib(40) << endl;
    cout << fibbonacci(40) << endl;
    cout << ortalama(100, 200, 300); << endl;
}
