#include <stdio.h>
#include <string.h>

int palindrome(long long x)
{
    long long original = x;
    long long reversed = 0;

    while (x)
    {
        reversed = reversed * 10 + x % 10;
        x /= 10;
    }

    return original == reversed;
}

int main()
{
    // int n;
    // scanf("%d", &n);

    while (1)
    {
        long long userIn;
        scanf("%lld", &userIn);

        if (userIn == 0)
        {
            return 0;
        }

        char p[4]; // "yes" 또는 "no"를 저장할 문자열 배열

        palindrome(userIn) ? strcpy(p, "yes") : strcpy(p, "no");

        printf("%s\n", p);
    }

    return 0;
}
