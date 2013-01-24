import os
import f1is
def main():

    args="dumbo start f1is.py -input access.log -output log.txt"
    args1 ="cat log.txt"
    args2 ="rm log.txt"
    os.system(args2)
    os.system(args)
    os.system(args1)

    #args2="dumbo start fis.py -hadoop /home/hadoop/hadoop-0.22.0/ -input input/access4.log -output ipcounts02 -overwrite yes"
    #args3 ="dumbo cat ipcounts02/part* -hadoop /home/hadoop/hadoop-0.22.0/ | sort -k2,2nr | head -n 20 >> log2.txt -overwrite yes"
    #os.system(args2)
    #os.system(args3)

main()


32	15167
38	15596
39	50675
41	14945
48	42135
32,38	11668
32,39	19795
38,39	21765
41,32	11929
41,38	12391
41,39	21358
41,48	19098
48,32	18926
48,38	19044
48,39	35883
32,39,41	5160
32,39,48	14055
32,41,48	4771
38,39,41	5700
38,39,48	14753
38,41,48	4983
39,41,48	15132



38	30987
39	56733
41	28779
48	49316
32,39	19795
38,39	21765
41,39	21358
41,48	19098
43141	0
45021	0
48,32	18926
48,38	19044
48,39	35883
4314.1	0
4502.1	0
39,41,48	15132

32	29875
38	30987
39	56733
41	28779
48	49316
32,38	11668
32,39	19795
38,39	21765
41,32	11929
41,38	12391
41,39	21358
41,48	19098
48,32	18926
48,38	19044
48,39	35883
32,39,41	9088
32,39,48	14055
32,41,48	8630
38,39,41	9722
38,39,48	14753
38,41,48	8760
39,41,48	15132



