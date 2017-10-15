// https://www.hackerrank.com/challenges/flipping-bits

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t;
    int temp;
    unsigned int l[150];
    cin >> t;
    for (int i=0; i<t; i++) {cin >> l[i];}
    for (int i=0; i<t; i++) {
        temp=~l[i];
        cout<<~l[i]<<endl;
    }
    return 0;
}

