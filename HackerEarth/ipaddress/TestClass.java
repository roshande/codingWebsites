/* IMPORTANT: Multiple classes and nested static classes are supported */

/*
 * uncomment this if you want to read input.
//imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility  classes
import java.util.*;
*/
import java.util.*;

class TestClass {
    public static void main(String args[] ) throws Exception {
        /*
         * Read input from stdin and provide input before running
         * Use either of these methods for input

        //BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int N = Integer.parseInt(line);

        //Scanner
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();

        for (int i = 0; i < N; i++) {
            System.out.println("hello world");
        }
        */
        Scanner s = new Scanner(System.in);
        String ipaddress=s.nextLine();
        String pattern = "^((0|1\\d?\\d?|2[0-4]?\\d?|25[0-5]?|[3-9]\\d?)\\.){3}(0|1\\d?\\d?|2[0-4]?\\d?|25[0-5]?|[3-9]\\d?)$";
        if(ipaddress.matches(pattern))
            System.out.println("YES");
        else
            System.out.println("NO");
            /*
        String [] ipnums = ipaddress.split(".",4);
        Boolean yes=true;
        for(String ipnum:ipnums)
            {
                //System.out.println(ipnum+ipnum.length());
                if(ipnum.charAt(0)=='0' && ipnum.length()>1)
                    {
                        yes=false;
                        break;
                    }
                int num = Integer.parseInt(ipnum);
                if(num>255 && num<0)
                    {
                        yes=false;
                        break;
                    }
            }
        if(yes==true)
            System.out.println("YES");
        else
            System.out.println("NO");*/
        //String ip_pattern = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        //System.out.println("Hello World!");
    }
}

