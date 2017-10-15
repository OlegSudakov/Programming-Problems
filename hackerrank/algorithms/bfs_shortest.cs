// https://www.hackerrank.com/challenges/bfsshortreach

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BFS
{
    class Program
    {
        class Node
        {
            int num, parent;
            public int distance = -1;
            public List<int> near = new List<int>();
            public Node(int num)
            {
                this.num = num;
            }
        }

        static void bfs(Node[] nodes, int s)
        {
            Queue<int> q = new Queue<int>();
            nodes[s].distance = 0;
            q.Enqueue(s);
            int current;
            while (q.Count > 0)
            {
                current = q.Dequeue();
                foreach (int node_num in nodes[current].near)
                {
                    if (nodes[node_num].distance == -1)
                    {
                        nodes[node_num].distance = nodes[current].distance + 6;
                        q.Enqueue(node_num);
                    }
                }

            }
            for (int i = 1; i < nodes.Length; i++)
            {
                if (i != s)
                {
                    Console.Write(nodes[i].distance.ToString() + ' ');
                }
            }
            Console.WriteLine();
        }

        static void Main(string[] args)
        {
            int t = Convert.ToInt32(Console.ReadLine());
            int n, m;
            int s;
            for (int i = 0; i < t; i++)
            {
                String[] temp = Console.ReadLine().Split(' ');
                n = Convert.ToInt32(temp[0]);
                Node[] nodes = new Node[n+1];
                for (int l = 0; l < n+1; l++)
                {
                    nodes[l] = new Node(l);
                }
                m = Convert.ToInt32(temp[1]);
                for (int j=0; j < m; j++)
                {
                    temp = Console.ReadLine().Split(' ');
                    int x = Convert.ToInt32(temp[0]);
                    int y = Convert.ToInt32(temp[1]);
                    nodes[x].near.Add(y);
                    nodes[y].near.Add(x);
                }
                s = Convert.ToInt32(Console.ReadLine());
                bfs(nodes, s);
            }
        }
    }
}

