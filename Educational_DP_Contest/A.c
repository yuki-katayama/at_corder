#include <stdio.h>

#define ABS(a) ((a) < 0 ? -(a) : (a))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int main(void) {
  int n, i, h;
  int price_last_2, price_last;
  int height_last_2, height_last;
  int price;
  scanf("%d", &n);
  scanf("%d%d", &height_last_2, &height_last);
  price_last_2 = 0;
  price_last = ABS(height_last - height_last_2);

  for(i = 2; i < n; i++) {
    h = 0;
    price = 0;
    scanf("%d", &h);
	price = MIN(price_last_2 + ABS(height_last_2 - h), price_last + ABS(height_last - h));

	price_last_2 = price_last;
	height_last_2 = height_last;
	price_last = price;
	height_last = h;
  }
  printf("%d", price_last);
  return 0;
}