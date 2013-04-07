#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define Length 30
struct wordOb
{
  char word[Length];
  struct wordOb* next;
};

struct hashOb
{
  long int hashnum;
  struct hashOb* next;
  struct wordOb* pto;
};

struct wordOb* wordlink = NULL;
struct hashOb* hashlink = NULL;
struct hashOb* hashlinkend = NULL;

char a[Length], b[Length];
int n, m;

struct hashOb* isearch(long h)
{
  struct hashOb* tmp = hashlink;
  while(tmp && tmp->hashnum - h){
    tmp = tmp->next;
  }
  return tmp;
}

long int ipow(int a, int b)
{
  long int ret=1;
  for(;b;b--)
    ret *= a;
}
long int hash(char * word)
{
  long int hashnum = 0;
  int c, i=1;
  while(c = *word)
    {
      hashnum += c * ipow(26, i);
      word ++;
      i ++;
    }
  return hashnum;
}

void init()
{
  int i;
  long int hashnum;
  struct hashOb *h1, *h2;
  struct wordOb *w1, *w2;
  scanf("%d %d", &n, &m);
  for(i = 0; i < m; i++)
    {
      w2 = (struct wordOb*)malloc(sizeof(struct wordOb));
      w2->next = NULL;
      scanf("%s %s", a, w2->word);
      hashnum = hash(a);
      if(hashlink && (h1 = isearch(hashnum)))
        {
          w1 = h1->pto;
          w1->next = w2;
        }
      else
        {
          w1 = (struct wordOb*)malloc(sizeof(struct wordOb));
          w1->next = w2;
          strcpy(w1->word, a);
          h1 = (struct hashOb*)malloc(sizeof(struct hashOb));
          h1->hashnum = hashnum;
          h1->pto = w1;
          if (!hashlink) hashlink = hashlinkend = h1;
          else {
            hashlinkend->next = h1;
            hashlinkend = h1;
          }
        }
      h2 = (struct hashOb*)malloc(sizeof(struct hashOb));
      h2->hashnum = hash(b);
      h2->pto = w1;
      hashlinkend->next = h2;
      hashlinkend = h2;
    }
  getchar();
}
void
solve()
{
  int i;
  struct hashOb *h;
  struct wordOb *w;
  while(scanf("%s", a))
    {
      if(h = isearch(hash(a)))
        {
          for(i = n-1, w = h->pto; w->next&&i; i--)
            {
              w = w->next;
            }
          printf(" %s", w->word);
        }
      else
        {
          printf(" %s", a);
        }
    }
  puts("");
}
int
main()
{
  int t, cas = 1;
  for(scanf("%d", &t); t--;) {
    printf("Case #%d:", cas++);
    init();
    solve();
  }
  return 0;
}
