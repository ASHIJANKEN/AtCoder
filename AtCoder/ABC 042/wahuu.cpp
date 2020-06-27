#include<iostream>
#include<string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    // Input numbers
    string a,b,c;
    cin >> a >> b >> c;

    vector<int> leng{stoi(a), stoi(b), stoi(c)};
    vector<int> haiku{5, 5, 7};
    sort(leng.begin(), leng.end());

    string ans = (leng == haiku) ? "YES" : "NO";
    cout << ans << endl;
    return 0;
}