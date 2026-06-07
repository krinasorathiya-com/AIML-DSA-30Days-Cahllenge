#include<iostream>
using namespace std;
int main()
{
    int age;
    cout<<"Enter your Age : ";
    cin>>age;
    if(age<0 || age>120)
    {
        cout<<"Please enter a valid age!"<<endl;
    }
    else if(age<18)
    {
        cout<<"You are not eligible for voting"<<endl;
    }
    else
    {
        cout<<"You are eligible for voting."<<endl;
    }
    return 0;
}
