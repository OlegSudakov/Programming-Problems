// https://www.hackerrank.com/challenges/pangrams

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pangrams
{
    struct ar_elem
    {
        public bool is_present;
        char letter;
        public ar_elem(char letter)
        {
            this.letter = letter;
            is_present = false;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            ar_elem[] letters = new ar_elem['z' - 'a' + 1];
            int i = 0;
            for (char letter = 'a'; letter <= 'z'; letter++)
            {
                letters[i] = new ar_elem(letter);
                ++i;
            }
            String input = Console.ReadLine().ToLower();
            foreach(char letter in input)
            {
                if(letter >= 'a' && letter <= 'z')
                {
                    letters[letter - 'a'].is_present = true;
                }
            }
            foreach(ar_elem letter_elem in letters)
            {
                if (letter_elem.is_present == false){
                    Console.WriteLine("not pangram");
                    Console.ReadLine();
                    return;
                }
            }
            Console.WriteLine("pangram");
            Console.ReadLine();
        }
    }
}

