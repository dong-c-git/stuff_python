#include <stdio.h>
#include <math.h>
int main()
{
    int x1,x2,x3,x4,x5;
    int y1,y2,y3,y4,y5;
    const int count = 5;
    const float zh = 0.3;
    const float mu = 0.7;
    float total;
    float average;
    x1 = 86;
    y1 = 81;
    x2 = 74;
    y2 = 87;
    x3 = 92;
    y3 = 90;
    x4 = 77;
    y4 = 62;
    x5 = 82;
    y5 = 88;
    total = (x1+x2+x3+x4+x5)*zh+(y1+y2+y3+y4+y5)*mu;
    average = total/count;
    printf("total=%.2f\n",total);
    printf("average=%.2f\n",average);
    printf("average=%d\n",(int)average);
    printf("I\n \nL\no\nv\ne\n \nG\nP\nL\nT\n");
    return 0;
}
