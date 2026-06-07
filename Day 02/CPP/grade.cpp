#include<iostream>
using namespace std;
int main(){
    int mark;
    cout<<"Enter your MARK:"<<endl;
    cin>>mark;
    if(mark<=0 || mark>100)
    {
        cout<<"Please enter valid marks!"<<endl;
    }
    else if(mark<60)
    {
        cout<<"Grade: F"<<endl;
        cout<<"You are fail in this exam."<<endl;
    }
    else if(mark<70)
    {
        cout<<"Grade: D"<<endl;
    }
    else if(mark<80)
    {
        cout<<"Grade: C"<<endl;
    }
    else if(mark<90)
    {
        cout<<"Grade: B"<<endl;
    }
    else
    {
        cout<<"Grade: A"<<endl;
        cout<<"EXCELLENT PERFORMANCE!"<<endl;
    }
    return 0;
}
