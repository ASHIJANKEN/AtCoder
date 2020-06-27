#include<iostream>
#include <cmath>
using namespace std;
int main()
{
    // Input numbers
    int n;
    cin >> n;
    long long a[n];
    for (int i = 0; i < n; i++) cin >> a[i];

    for (int i = 0; i < n; i++) {
        if (a[i] == 0) {
            cout << 0 << endl;
            return 0;
        }
    }

    long long ans = 1;
    for (int i = 0; i < n; i++) {
        if (a[i] <= 1000000000000000000 / ans) {
            ans *= a[i];
        } else {
            cout << -1 << endl;
            return 0;
        }
    }

    cout << ans << endl;
    return 0;
}
