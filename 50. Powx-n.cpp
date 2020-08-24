#include <iostream>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        // ugly edge cases
        if (x == 1) {
            return 1;
        }
        if (x == -1) {
            if (n % 2 == 0) {
                return 1;
            } else {
                return -1;
            }
        } else if (n == 0) {
            return 1;
        } else if (n == INT_MIN) {
            return 0;
        }
        double part;
        if (n % 2 == 0 && n >= 0) {
            part = myPow(x, n / 2);
            return part * part;
        } else if (n % 2 == 1 && n >= 0) {
            part = myPow(x, (n - 1) / 2);
            return part * part * x;
        } else {
            part = myPow(x, -n);
            return 1/part;
        }
    }
};
