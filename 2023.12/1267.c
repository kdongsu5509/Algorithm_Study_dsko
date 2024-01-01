#include <stdio.h>
#include <string.h>

typedef long long lang;

int main()
{
    int n;
    scanf("%d", &n);

    int telTime[20] = {0};

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &telTime[i]);
    }

    int case1 = 0;
    int case2 = 0;

    for (int i = 0; i < n; i++)
    {
        if (telTime[i] == 0)
        {
            break;
        }
        else
        {
            case1 += ((telTime[i] / 30) + 1) * 10;
            case2 += ((telTime[i] / 60) + 1) * 15;
        }
    }

    if (case1 == case2)
    {
        printf("Y M %d\n", case1);
    }
    else if (case1 > case2)
    {
        printf("M %d\n", case2);
    }
    else
    {
        printf("Y %d\n", case1);
    }

    return 0;
}