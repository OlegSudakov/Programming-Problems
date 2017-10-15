// https://www.hackerrank.com/challenges/insertionsort1

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace insertion_sort_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int array_size = Convert.ToInt32(Console.ReadLine());
            int [] array = new int[array_size];
            string[] arr_temp = Console.ReadLine().Split(' ');
            array = Array.ConvertAll(arr_temp, Int32.Parse);
            int e = array[array_size-1];
            for (int i = array_size-1; i>0; i--)
            {
                if (array[i-1] < e)
                {
                    array[i] = e;
                    foreach (int item in array)
                    {
                        Console.Write(item.ToString() + ' ');
                    }
                    return;
                }
                else
                {
                    array[i] = array[i - 1];
                }
                foreach (int item in array)
                {
                    Console.Write(item.ToString() + ' ');
                }
                Console.WriteLine();
            }
            array[0] = e;
            foreach (int item in array)
            {
               Console.Write(item.ToString() + ' ');
            }
            Console.Read();
        }
    }
}
