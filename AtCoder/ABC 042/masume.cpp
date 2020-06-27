#include<iostream>
using namespace std;


long fact(long num)
{
    long ret = 1;
    for (int i = 1; i <= num; ++i) {
        ret *= i;
    }
    return ret;

    // if (num == 0) return 1;
    // return num * fact(num - 1);
}

int main()
{
    // Input numbers
    long h, w, a, b;
    cin >> h >> w >> a >> b;

    long cnt = 0;
    for (int i = 0; i < h-a; ++i) {
        long left_comb = fact(i + (b - 1)) / (fact(i) * fact(b - 1));
        long right_comb = fact((h - i - 1) + (w - b - 1)) / (fact(h - i - 1) * fact(w - b - 1));
        // cout << "l:" << left_comb << " r:" << right_comb << endl;

        cnt += left_comb * right_comb;
    }

    // Output
    cout << cnt % 1000000007 << endl;
    return 0;
}
