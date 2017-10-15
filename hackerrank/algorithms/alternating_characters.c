// https://www.hackerrank.com/challenges/alternating-characters

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int len(char s[]){
	int l = 0;
	int i = 0;
	while (s[i] != '\0') {
		l++;
		i++;
	}
	return l;
};

int main()
{
	char s[150000];
	int res[15];
	for (int i = 0; i < 15; i++){
		res[i] = 0;
	}
	int l;
	

	int t;
	char prev;
	cin >> t;
	for (int i = 0; i < t; i++){
		cin >> s;
		prev = s[0];
		l = len(s);
		for (int j = 1; j < l; j++) {
			if (s[j] == prev) res[i]++;
			else prev = s[j];
		}
	}
	for (int i = 0; i < t; i++){
		cout << res[i] << '\n';
	}
	return 0;
}

