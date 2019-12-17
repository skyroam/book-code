package chapter4;

import java.util.Scanner;

public class Test2
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        for(int i = 0; i < num; i++)
        {
            for(int j = 0; j < num-i; j++)
            {
                System.out.print(' ');
            }
            for(int k = 0; k < 2*i+1; k++)
            {
                System.out.print('*');
            }
            // for(int j = 0; j < num-i; j++)
            // {
            //     System.out.print(' ');
            // }
            System.out.println();
        }
    }
}