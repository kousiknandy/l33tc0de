#include "stdio.h"
#include "stdlib.h"

#define XSTR(A) STR(A)
#define STR(A) #A
#define CT_MAX_SN_LENGTH 4

int main(int ac, char **av)
{
  FILE *fp;
  char *s = malloc(CT_MAX_SN_LENGTH+1);
  if (!s) return -1;
  s[CT_MAX_SN_LENGTH] = '\0';
  fp = popen("cat fscanf.c", "r");
  if (!fp) return -1;
  fscanf(fp, "%" XSTR(CT_MAX_SN_LENGTH) "s", s);
  pclose(fp);
  puts(s);
  return 0;
}
    
