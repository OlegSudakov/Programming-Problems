// https://www.hackerrank.com/challenges/fibonacci-modified

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;



namespace FibonacciModified
{
    class Program
    {
        static void Main(string[] args)
        {
            int a, b, n;
            String[] temp_s = Console.ReadLine().Split(' ');
            a = Convert.ToInt32(temp_s[0]); b = Convert.ToInt32(temp_s[1]); n = Convert.ToInt32(temp_s[2]);
            BigInteger cur = new BigInteger(b);
            BigInteger prev = new BigInteger(a);
            BigInteger temp;
            int cur_n = 2;
            while (cur_n < n)
            {
                temp = BigInteger.Add(BigInteger.Multiply(cur, cur), prev);
                prev = cur;
                cur = temp;
                cur_n++;
            }
            Console.WriteLine(cur.ToString());
            Console.ReadLine();
        }
    }
}

