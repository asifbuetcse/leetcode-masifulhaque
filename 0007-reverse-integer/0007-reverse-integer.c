int reverse(int x){
  if (x < INT_MIN || x > INT_MAX) {
    return 0;
  }
  int reversed = 0;
  while (x != 0) {
    if (reversed < INT_MIN/10 || reversed > INT_MAX/10) {
      return 0;
    }
    reversed = reversed * 10 + x % 10;
    x /= 10;
  }
  return reversed;
}