// https://www.hackerrank.com/challenges/maximizing-xor

#include <stdio.h>
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int l;
	int r;
	cin >> l;
	cin >> r;
	int max = 0;
	for (int i = l; i <= r; i++)
		for (int j = l; j <= r; j++) {
			if (int(i^j) > max) max = i^j;
	}
		cout << max;

	return 0;
}
