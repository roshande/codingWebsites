#include<stdio.h>

int main()
{
	printf("abcde / fghij = N\n");
	for(int N=2;N<=80;++N)
	{
		for(int fghij=1234;fghij<=(98765/N);++fghij)
		{
			int abcde = fghij *N;
			short used=(fghij < 10000);
			int temp=abcde;while(temp){ used |= (1 <<(temp%10)); temp/=10; }
			temp=fghij;    while(temp){ used |= (1 <<(temp%10)); temp/=10; }
			if(used == (1<<10)-1)
				printf("%0.5d / %0.5d = %d\n",abcde,fghij,N);
		}
	}
	return 0;
}
