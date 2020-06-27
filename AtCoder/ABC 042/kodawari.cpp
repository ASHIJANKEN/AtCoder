#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;

// int main()
// {
//     int n,k;
//     cin >> n >> k;

//     vector<int> d;
//     for (int i = 0; i < k; ++i) {
//         int a;
//         cin >> a;
//         d.push_back(a);
//     }

//     vector<int> nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
//     vector<int> available_num;
//     std::set_difference(nums.begin(), nums.end(), d.begin(), d.end(), std::back_inserter(available_num));

//     int ans = 0;

//     for (int i = 0; (int)(n / (int)pow(10, i)) > 0; i++) {
//         int pow10 = (int)pow(10, i);

//         int digit = (int)(n / pow10) % 10;

//         int found = 0;
//         for (int x : available_num) {
//             if (x >= digit) {
//                 ans += x * pow10;
//                 found = 1;
//                 break;
//             }
//         }

//         if (digit == 9 && found == 0) {
//             n = n + 1 * pow10;
//             i--;
//         }
//     }

//     cout << ans << endl;
//     return 0;
// }

int main()
{
    int n,k;
    cin >> n >> k;

    vector<int> d;
    for (int i = 0; i < k; ++i) {
        int a;
        cin >> a;
        d.push_back(a);
    }

    int ans = 0;

    while(true) {
        int n_check = n;
        int kodawari_found = 0;
        while(n_check > 0) {
            int digit = n_check % 10;

            auto itr = std::find(d.begin(), d.end(), digit);
            if( itr != d.end() ) {
                kodawari_found = 1;
                break;
            }

            n_check /= 10;
        }

        if (kodawari_found == 0) {
            ans = n;
            break;
        }

        n++;
    }

    cout << ans << endl;
    return 0;
}