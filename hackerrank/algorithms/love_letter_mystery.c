// https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

#include <stdio.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int len(char s[]){
	int i = 0;
	while (s[i] != '\0') {
		i++;
	}
	return i;
};

int main()
{
	char s[15000];
	int res[15];
	int l;
	int b;
	int t;
	cin >> t;
	for (int i = 0; i < t; i++){
		res[i] = 0;
	}
	for (int i = 0; i < t; i++){
		cin >> s;
		l = len(s);
		b = len(s) / 2;
		for (int j = 0; j < b; j++){
			res[i] += abs(int(s[j] - s[l - 1 - j]));
		}

	}
	for (int i = 0; i < t; i++){
		cout << res[i] << '\n';
	}
	return 0;
}
