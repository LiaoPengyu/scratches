void
Qsort(int * const a, int left, int right)
{
  int l = left, h = right, m = left;
  int pivot = a[l + rand() % (h-l+1)];
  while( m<=h )
    {
      int x = a[m] - pivot;
      switch( (x>0) - (x<0) )
        {
          case -1: swap(a, l++, m++); break;
          case  0: m++; break;
          case  1: swap(a, m, h--); break;
        }
      Qsort(a, left, l-1);
      Qsort(a, m, right);
    }
}
