// https://www.hackerrank.com/challenges/utopian-tree

#include <iostream>
using namespace std;

int height(int n) {
    int k=1;
    for (int i=0; i<n/2; i++) {
        k=k*2;
        k++;
    }
    if (n%2==1) {k=k*2;}
    return k;
}
int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        cout << height(n) << endl;
    }
}

