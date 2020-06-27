// #include<iostream>
// #include <string>
// #include <math.h>

// using namespace std;
// typedef long long int lli;

// int main()
// {
//     // Input numbers
//     int n;
//     cin >> n;
//     lli ans = 0;

//     for (int i = 1; i <= n; ++i) {
//         double sq = sqrt(i);
//         int count = 0;
//         int last_yakusuu;
//         for( int j = 1; (double)j <= sq; ++j ){
//             if( i % j == 0 ) {
//                 count++;
//                 last_yakusuu = j;
//             }
//         }

//         int yakusuu = ((double)last_yakusuu != sq) ? count * 2 : count * 2 - 1;

//         cout << yakusuu << endl;
//         ans += i * yakusuu;
//     }

//     cout << ans << endl;
//     return 0;
// }

#include<iostream>
#include <string>
#include <math.h>

using namespace std;
typedef long long int lli;


lli yaku(int num) {
    if(num == 1) return 1;
    if(num == 2 || num == 3) return 2;

    double sq = sqrt(num);
    int count = yaku((int)sq);

    return (num % (int)sq == 0) ? count * 2 - 1 : count * 2;
}



int main()
{
    // Input numbers
    int n;
    cin >> n;
    lli ans = 0;

    for (int i = 1; i <= n; ++i){
        lli y = yaku(i);
        ans += i * y;
        cout << y << endl;
    }

    cout << ans << endl;
    return 0;
}


// #include<iostream>
// #include <string>
// #include <math.h>

// using namespace std;
// typedef long long int lli;


// lli yaku(int num) {
//     cout << "yaku num: " << num << endl;
//     if(num == 1) return 1;
//     if(num == 2 || num == 3) return 2;

//     double sq = sqrt(num);
//     int count = yaku((int)sq);

//     int y = (num % (int)sq == 0) ? count * 2 - 1 : count * 2;

//     cout << "y: " << y << endl;

//     return y;
// }



// int main()
// {
//     // Input numbers
//     int n;
//     cin >> n;


//     cout << yaku(n) << endl;
//     return 0;
// }