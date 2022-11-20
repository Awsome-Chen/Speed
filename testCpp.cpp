#include<iostream>
#include<ctime>
using namespace std;

int isPrime(int number) {
  for (int x = 2; x < number; x++) {
    if ((number % x) == 0) {
      return false;
    }
  }
  return true;
}

int main()
{
  clock_t startTime = clock();
  int count = 0;
  for (int x = 1; x <= 100000; x++) {
    if (isPrime(x)) {
      count++;
    }
  }
  cout << "1000000以内质数的个数是 " << count << endl;
  clock_t endTime = clock();
  cout << "整个程序用时：" << double(endTime - startTime) / CLOCKS_PER_SEC << "s" << endl;
  system("pause");
  return 0;
}