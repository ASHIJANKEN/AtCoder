#include<iostream>
#include <string>

using namespace std;
typedef long long int lli;

int main()
{
    // Input numbers
    string s, t;
    cin >> s >> t;

    lli count = 0;
    for (lli i = 0; i < (lli)s.size(); ++i) {
        if (s[i] != t[i]) {
            count++;
        }
    }

    cout << count << endl;
    return 0;
}