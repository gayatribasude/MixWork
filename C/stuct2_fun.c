#include<stdio.h>
#include<string.h>




struct St{
	int roll;
	char name[60];
}s1,s2;

void display(struct St s){
	printf("display: %d\t%s",s.roll,s.name);
}


int main(){
	
	s1.roll=34;
	strcpy(s1.name,"sdjsahdc");
	

	s2=s1;
	

	display(s1);
	return 10;

}