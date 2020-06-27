#include<iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;

    string ans("");
    for (int i = 0; i < (int)s.length(); ++i) {
        char key = s[i];

        if (key == 'B') {
            if (!ans.empty()) {
                ans.pop_back();
            }
        } else {
            ans += key;
        }
    }

    cout << ans << endl;
    return 0;
}