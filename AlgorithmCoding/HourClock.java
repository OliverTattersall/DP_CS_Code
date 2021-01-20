package DP_CS_Code.AlgorithmCoding;
import java.util.Scanner;

class HourClock{

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String[] times = s.nextLine().split(",");
        int h = Integer.parseInt(times[0]);
        String m = times[1];
        String c;

        if(h>12){
            c=" PM";
            h=h-12;

        }else{
            c=" AM";
        }
        String answer = h+":"+m+c;
        System.out.print(answer+"\n");
        s.close();
    }
}