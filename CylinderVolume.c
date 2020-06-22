#include <stdio.h>
int main()
{
	//float pie = 3.142;
	float radius, height, volume;
	scanf("%f%f", &radius, &height);
	volume = 3.142 *radius * radius *height;
	printf("%f", volume);
}