#include <iostream>
using namespace std;

void RecPermute(string soFar, string rest)
{
  if (rest == "")
  {
    std::cout << soFar << std::endl;
  } else {
        for (int i = 0; i < rest.length(); i++) {
          // append on the next letter to what we've seen so far
          std::string next = soFar + rest[i];
          std::string remaining = rest.substr(0,i) +
                             rest.substr(i+1);
          RecPermute(next, remaining);
        }
    }
}

void ListPermutations(string s)
{
  RecPermute("", s);
}

int main()
{
  ListPermutations("abcd");
}