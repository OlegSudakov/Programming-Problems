// https://www.hackerrank.com/challenges/insertionsort2

using System;
using System.Collections.Generic;
using System.IO;
class Solution
{
    static void insertionSort(int[] ar)
    {
        int cur_elem_ind = 1;
        while (cur_elem_ind < ar.Length) {
            int e = ar[cur_elem_ind];
            bool ins_flag = false;
            for (int i = cur_elem_ind; i>0; i--)
            {
                if (ar[i-1] < e)
                {
                    ar[i] = e;
                    ins_flag = true;
                    break;
                }
                else
                {
                    ar[i] = ar[i - 1];
                }
            }
            if (!ins_flag)
            {
                ar[0] = e;
            }
            foreach (int item in ar)
            {
                Console.Write(item.ToString() + ' ');
            }
            Console.WriteLine();
            cur_elem_ind++;
        }
        
    }

    static void Main(String[] args)
    {
        int _ar_size;
        _ar_size = Convert.ToInt32(Console.ReadLine());
        int[] _ar = new int[_ar_size];
        String elements = Console.ReadLine();
        String[] split_elements = elements.Split(' ');
        for (int _ar_i = 0; _ar_i < _ar_size; _ar_i++)
        {
            _ar[_ar_i] = Convert.ToInt32(split_elements[_ar_i]);
        }
        insertionSort(_ar);
    }
}

