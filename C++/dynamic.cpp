# include<iostream>

using namespace std;

int climbStairs(int n)
{
    if (n == 1):
    {
        return 1;
    }
    if (n == 2):
    {
        return 2;
    }
    int f1 = 1, f2 = 2, res;
    for (int i = 3; i<=n; i++)
    {
        res = f1 + f2;
        f1 = f2;
        f2 = res;
    }
    return res;
}
int main()
{
   climbStairs(4);

   return 0;
}
