#include <iostream>
using namespace std;

int main()
{
    int n = 10;

    for (int i = 0; i < n; i++)
    {
        if (i == 0 || i == n - 1)
        {
            for (int j = 0; j < n; j++)
                cout << "*";
        }
        else
        {
            int left = (n / 2) - i;
            if (left < 1)
                left = i - (n / 2) + 1;

            int right = left;

            for (int j = 0; j < left; j++)
                cout << "*";

            int spaces = n - left - right;
            for (int j = 0; j < spaces; j++)
                cout << " ";

            for (int j = 0; j < right; j++)
                cout << "*";
        }

        cout << endl;
    }

    return 0;
}