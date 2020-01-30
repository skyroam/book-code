package chapter4;

import java.util.Scanner;


public class Test3
{
    public static void main(String[] args) 
    {
        Scanner in = new Scanner(System.in);
        System.out.println("Please input a number:");
        float radius = in.nextFloat();
        //float diameter = 2 * radius;
 
        for(float j = radius; j > 0; j--)
        {    
            double dis = Math.sqrt(radius*radius - j*j);
            for(int i = 0; i < (int)(2*radius); i ++)
            {   
                //System.out.println(i);
                //System.out.println(radius-dis);
                //System.out.println(radius+dis);
                if(i == (int)(radius-dis) || i == (int)(radius+dis)) 
                {
                    System.out.print('*');
                }
                else
                {
                    System.out.print(' ');
                }
                
            }
            System.out.println();
        }

        for(float j = 1; j < radius; j++)
        {    
            double dis = Math.sqrt(radius*radius - j*j);
            for(int i = 0; i < (int)(2*radius); i ++)
            {
                if(i == (int)(radius-dis) || i == (int)(radius+dis)) 
                {
                    System.out.print('*');
                }
                else
                {
                    System.out.print(' ');
                }
                
            }
            System.out.println();
        }

    }
}