#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define Length 30
#define SentLen 300
struct wordOb
{
  char word[Length];
  struct wordOb* next;
};

struct hashOb
{
  struct hashOb* next;
  struct wordOb* pto;
};

struct hashOb* hashlink = NULL;
struct hashOb* hashlinkend = NULL;

char a[Length], b[Length];
char sentence[SentLen];
int n, m;

struct hashOb* isearch(char* s)
{
  struct hashOb* tmp = hashlink;
  while(tmp && strcmp(tmp->pto->word, s)){
    tmp = tmp->next;
  }
  return tmp;
}

void iclearp()
{
  struct hashOb *tmp, *h=hashlink;
  while (h) {
      tmp = h;
      h = h->next;
      free(tmp->pto);
      free(tmp);
    }
}
void init()
{
  int i;
  struct hashOb *h1, *h2;
  struct wordOb *w1, *w2;
  iclearp();
  scanf("%d %d", &n, &m);

  for(i = 0; i < m; i++)
    {
      w2 = (struct wordOb*)malloc(sizeof(struct wordOb));
      w2->next = NULL;
      scanf("%s %s", a, w2->word);
      if(hashlink && (h1 = isearch(a)))
        {
          w1 = h1->pto;
        }
      else
        {
          w1 = (struct wordOb*)malloc(sizeof(struct wordOb));
          strcpy(w1->word, a);
          h1 = (struct hashOb*)malloc(sizeof(struct hashOb));
          h1->pto = w1;
          h1->next = NULL;
          if (!hashlink) {
            hashlink = hashlinkend = h1;
          }
          else {
            hashlinkend->next = h1;
            hashlinkend = h1;
          }
        }
      if(h2 = isearch(w2->word)){
        w2 = h2->pto;
      }
      else{
        h2 = (struct hashOb*)malloc(sizeof(struct hashOb));
        h2->pto = w2;
        h2->next = NULL;
        hashlinkend->next = h2;
        hashlinkend = h2;
      }
      w1->next = w2;
    }
  getchar();
}
void
solve()
{
  int i;
  struct hashOb *h;
  struct wordOb *w;
  char* iword;

  //
  h = hashlink;
  while(h){
    h = h->next;
  }
  fgets(sentence, SentLen, stdin);
  for (iword = strtok(sentence, " \n\r");
       iword;
       iword = strtok(NULL, " \n\r"))
    {
      if(h = isearch(iword))
        {
          for(i = n-1, w = h->pto; w->next&&i; i--)
            {
              w = w->next;
            }
          printf(" %s", w->word);
        }
      else
        {
          printf(" %s", iword);
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
