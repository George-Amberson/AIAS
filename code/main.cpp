#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <chrono>
#include <time.h>
#include <exception>
void generate_strings( std::string& generate_str, std::stringstream& input) {
	int type;
	srand(time(NULL)); 
	std::string letters;
	int length;
	input >> type >> letters >> length;
	if (type == 2) {
		generate_str.resize(length);
		for (int i = 0; i < length; i++) {
			generate_str[i] = letters[rand() % letters.length()];
		}
	}
	else {
		
		for (int i = 0; i < length; i ++) {
			generate_str += letters;
		}
	}
}
void TextFromClipboard(std::string& substr, std::string& str)
{
	
	if (OpenClipboard(0))//открываем буфер обмена
	{
		 HANDLE hdata = GetClipboardData(CF_TEXT);
		 char* hbuff = static_cast<char*>(GlobalLock(hdata));
		 std::stringstream text(hbuff);
		 GlobalUnlock(hdata);
		 CloseClipboard();
		 int type;
		 text >> type;
		 if (type) {
			 generate_strings(str, text);
			 generate_strings(substr, text);

		 }else text >> substr >> str;
	}
	return;
}

double NativeAlgorithm( std::string& substr,  std::string& str) {
	auto begin = std::chrono::high_resolution_clock::now();
	std::vector<int>func;
	for (long int i = substr.length(); i < str.length(); i++) {
		long int s = 0;
		while (substr[s] == str[i - (substr.length() - s)] && s < substr.length()) {
			s++;
		}
		if (s == substr.length() &&
			substr[substr.length()] == str[i])
			func.push_back(substr.length());
		else
			func.push_back(0);
	}
	auto end = std::chrono::high_resolution_clock::now();
	return std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count();
}
void prefix_func(std::string& substr, std::vector<int>& z) {
	int length = substr.length() > 0 ? substr.length() : 1;
	z.resize(length);
	z[0] = 0;
	for (int i = 1; i < z.size(); ++i) {
		int pos = z[i - 1];
		while (pos > 0 && substr[pos] != substr[i])
			pos = z[pos - 1];
		z[i] = pos + (substr[pos] == substr[i] ? 1 : 0);
	}
}
double KMPAlgorithm(std::string& str, std::string& substr) {
	std::vector<int> z;
	auto begin = std::chrono::high_resolution_clock::now();
	prefix_func(substr, z);
	int pos = 0;
	for (int i = 0; i < str.length(); ++i) {
		while (pos > 0 && (pos >= substr.length() || substr[pos] != str[i]))
			pos = z[pos - 1];
		if (str[i] == substr[pos]) pos++;
	}
	auto end = std::chrono::high_resolution_clock::now();
	return std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count();
}
int main() {

	std::string str;
	std::string substr;
	std::vector<int>ans1, ans2;
	double r1, r2;
	TextFromClipboard(substr, str);
	r1 = 0;
	r2 = 0;
	r1=NativeAlgorithm(substr, str);
	r2 = KMPAlgorithm(substr, str);
	///std::cout << str.size() << " " << substr.size();
	std::cout << r1<<" "<<r2;

	return 0;

}