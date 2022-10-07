#include <iostream>

using namespace std;

using LLI = long long int;

LLI qpow(int x, int y) {
    LLI tmp_x = x, result = 1;
    while (y > 0) {
        if (y & 1) { // 若 y 为奇数
            result *= tmp_x;
        }
        y >>= 1;
        tmp_x = tmp_x * tmp_x;
    }
    return result;
}

// LLI table[100000] = {0};

int main() {
    int T;
    cin >> T;
    while (T--) {
        LLI x;
        cin >> x;
        int cont = 0;
        int memo[10] = {0};
        while (x) {
            int i = 1;
            LLI p = 1;
            if (x > 0) {
                while (p < x) {
                    i += 1;
                    p = qpow(i, 2);
                }
                x -= p;
            } else {
                while (p < -x) {
                    i += 1;
                    p = qpow(i, 2);
                }
                x += p;
            }
            cont += 1;
            memo[cont] = i;
        }
        cout << cont << " " << endl;
        for (int i = 0; i < cont; i++) {
            cout << memo[i] << " ";
        }
    }


    return 0;
}