#include <iostream>
#include <stdlib.h>

// Recursive is palindrome
bool isPal(std::string s)
{
  if (s.length() <= 1) return true;
  return (s[0] == s[s.length() - 1] &&
    isPal(s.substr(1, s.length() -2))); 
}

int main() {  
  std::cout << ispal("racecar") << "\n";
}