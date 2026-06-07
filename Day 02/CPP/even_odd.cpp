#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"The number is ";
    cin>>n;
    cout<<"The number is "<<n<<" and it is ";
    if(n%2==0){
        cout<<"Even";
    }
    else{
        cout<<"Odd";
    }
    return 0;
}

