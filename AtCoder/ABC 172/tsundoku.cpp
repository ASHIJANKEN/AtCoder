#include<iostream>
#include <string>
#include <deque>

using namespace std;
typedef long long int lli;

int main()
{
    // Input numbers
    int n, m, k;
    cin >> n >> m >> k;

    deque<int> a;
    deque<int> b;
    for (int i = 0; i < n; ++i) {
        int tmp;
        cin >> tmp;
        a.push_back(tmp);
    }
    for (int i = 0; i < m; ++i) {
        int tmp;
        cin >> tmp;
        b.push_back(tmp);
    }

    lli elapsed_time = 0;
    int count = 0;
    // int same_count = 0;
    // bool same, same_which = false, false;
    while(true) {
        int inc;

        if(a.empty() && b.empty()) {
            break;
        } else if (a.empty() != b.empty()) {
            if (a.empty()) {
                inc = b[0];
                b.pop_front();
            } else {
                inc = a[0];
                a.pop_front();
            }
        } else {
            if(a[0] == b[0]) {
                int same_count = 0;
                bool is_a = true;
                for (int i = 0; ; ++i) {
                    if((int)a.size() > i && (int)b.size() > i) {
                        if (a[i] == b[i]) {
                            same_count++;
                        } else {
                            if (a[i] > b[i]) is_a = false;
                            break;
                        }
                    } else if ((int)a.size() <= i || (int)b.size() <= i) {
                        if ((int)a.size() <= i) is_a = false;
                        break;
                    } else {
                        break;
                    }
                }

                if (is_a == true) {
                    for (int i = 0; i < same_count; ++i) {
                        if (elapsed_time + a[0] <= k) {
                            elapsed_time += a[0];
                            a.pop_front();
                            count++;
                        } else break;
                    }

                    inc = a[0];
                    a.pop_front();
                } else {
                    for (int i = 0; i < same_count; ++i) {
                        if (elapsed_time + b[0] <= k) {
                            elapsed_time += b[0];
                            b.pop_front();
                            count++;
                        } else break;
                    }

                    inc = b[0];
                    b.pop_front();
                }
            } else {
                // same = false;
                if (a[0] > b[0]) {
                    inc = b[0];
                    b.pop_front();
                } else {
                    inc = a[0];
                    a.pop_front();
                }
            }
        }

        if (elapsed_time + inc > k) {
            break;
        } else {
            elapsed_time += inc;
            count++;
        }
    }

    cout << count << endl;
    return 0;
}