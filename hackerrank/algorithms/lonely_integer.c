// https://www.hackerrank.com/challenges/lonely-integer

#include <stdio.h>
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int a[150];
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	int x = 0;
	for (int i = 0; i < n; i++) {
		x = x^a[i];
	}
	cout << x;
	return 0;
}
