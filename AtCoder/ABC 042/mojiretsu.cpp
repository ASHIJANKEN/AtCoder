#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int n,l;
    cin >> n >> l;

    vector<string> s;
    for (int i = 0; i < n; ++i) {
        string a;
        cin >> a;
        s.push_back(a);
    }

    sort(s.begin(), s.end());

    string ans = "";
    for (int i = 0; i < n; ++i) {
        ans += s[i];
    }

    cout << ans << endl;
    return 0;
}