#include <iostream>
using namespace std;

int main() {
    int n = 5;

    for (int i = 1; i <= n; i++) {

        // Spaces
        for (int j = 1; j <= n - i; j++) {
            cout << "  ";
        }

        // Characters
        for (char ch = 'A' + n - i; ch <= 'E'; ch++) {
            cout << ch << " ";
        }

        cout << endl;
    }

    return 0;
}