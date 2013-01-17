int
MaxSubsequenceSum( const int seq[], int N )
{
  int tmpSum, MaxSum, j;

  tmpSum = MaxSum = 0;
  for( j=0; j<N; j++ ) {
    tmpSum += seq[j];

    if( tmpSum > MaxSum ) 
      MaxSum = tmpSum;
    else if( tmpSum < 0 ) 
      tmpSum = 0;        
  }                         
  return MaxSum;                 
}
