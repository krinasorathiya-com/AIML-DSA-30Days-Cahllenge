#include <iostream>
using namespace std;

int main() {
    int n = 4;

    for (int i = 1; i <= n; i++) {

        // Increasing letters
        for (char ch = 'A'; ch < 'A' + i; ch++) {
            cout << ch;
        }

        // Decreasing letters
        for (char ch = 'A' + i - 2; ch >= 'A'; ch--) {
            cout << ch;
        }

        cout << endl;
    }

    return 0;
}