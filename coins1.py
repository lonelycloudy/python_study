递归 换零钱问题——由打靶子问题引申

using System;
//using System.Collections.Generic;
//using System.Text;
/*有任意张1毛，2毛，5毛钱，有几种组合可以组成9毛钱的方法。用递归实现并输出各种组合方法。*/
namespace digui1
{
    public class Class3
    {
        public static int sum = 0;
        public static int[] a = new int[] { 1, 2, 5 };
        public static int[] store = new int[9];
        public static void Main()
        {
            fun(9, 0);
            Console.WriteLine("总数为{0}", sum);
            Console.ReadLine();
        }

        public static void fun(int money, int k)
        {
            if (money< 0)
                return;
            if (money == 0)
            {
                Output(k);
                return;
            }
            for (int i = 0; i < 3; i++)
            {
                if (k == 0 || (k > 0 && a[i]>= store[k - 1]))//递增输出防止重复
                {
                    store[k] = a[i];
                    fun(money - a[i], k + 1);
                }
            }
        }
        public static void Output(int k)
        {
            for (int i = 0; i < k; i++)
            {
                Console.Write("{0} ", store[i]);
            }
            Console.WriteLine();
            sum++;
        }
    }
}
