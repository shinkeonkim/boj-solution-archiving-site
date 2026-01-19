#include "timecard.h"

void init(int n) {

}

std::string convert(std::string s) {
  std::string ret = "";
  
  for(auto i : s) {
    if('a' <= i && i <= 'z') {
      ret += i;
    } else if('A' <= i && i <= 'Z') {
      ret += char(i - 'A' + 97);
    } else {
      ret += i;
    }
  }
    
  return ret;
}
