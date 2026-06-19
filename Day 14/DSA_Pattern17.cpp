#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 4; i++) {
        for (char ch = 'A'; ch < 'A' + i; ch++) {
            cout << ch;
        }
        for (char ch = 'A' + i - 2; ch >= 'A'; ch--) {
            cout << ch;
        }

        cout << endl;
    }

    return 0;
}