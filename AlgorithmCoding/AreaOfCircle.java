package DP_CS_Code.AlgorithmCoding;
import java.util.Scanner;

class AreaOfCircle{

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String[] coords= s.nextLine().split(" ");
        float [] fcoords = new float[4];
        for(int i = 0;i<4;i++){
            // System.out.print(coords[i]+"\n");
            fcoords[i]= Float.parseFloat(coords[i]);
        }
        // System.out.print("helloworld\n");

        float r2;
        float pi=3.14159f;
        r2 = (fcoords[2]-fcoords[0])*(fcoords[2]-fcoords[0]) + (fcoords[3]-fcoords[1])*(fcoords[3]-fcoords[1]);

        float a;
        a=pi*r2;
        String answer = Float.toString(a);
        System.out.print(answer+'\n');
        s.close();
    }
}