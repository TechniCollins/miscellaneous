#include <stdio.h>
#define CLASS_POPULATION 3
int main()
{
	int counter = 1, marks, total, counter2 = 1;
	while (counter2 < CLASS_POPULATION)
	{
		printf("\nEnter all the marks for Student %d", counter2);	
		while (counter < 4)
		{
			printf("\nEnter marks for unit %d: ", counter);
			scanf("%d", &marks);
			total = total + marks;
			counter = counter +1;
			printf("\nRunning Total is %d", total);
		}
		counter = 0;
		counter2 = counter2 +1;
		
	}
	
}