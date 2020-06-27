#include<iostream>
#include <cmath>
using namespace std;
int main()
{
    // Input numbers
    long long a;
    double b;
    cin >> a >> b;

    long long b_100 = round(b*100);

    // Output
    cout << (long long)((a*b_100)/100) << endl;
    return 0;
}
