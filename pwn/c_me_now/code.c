// This is a program to generate your own valentine! It's like, super secure. I bet you won't find any bugs. 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char poem[255];
 
int make_valentine() {
  printf("🌹 🌹 🌹 🌹 🌹 🌹 \n");
  printf("Roses are red,\n");
  printf("Violets are blue, \n");
  printf("Sugar is sweet, \n");
  // User input:
  printf("%s", poem);
  printf("🌹 🌹 🌹 🌹 🌹 🌹 \n");
  return 0;
}
 
int main(int argv, char* argc[]) {
  printf("Welcome to the Valentine Generator! \n");
  printf("Please enter the next line of the poem:\n");
  fgets(poem, 255, stdin);
  int ret = make_valentine();
  memset(poem, 0x00, sizeof(poem));
  return ret;
}
