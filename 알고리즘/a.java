import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();

        int l = sc.length();

        String newthing = "";
        for (i = 0; i < l; i++) {
            if (newthing[i] >= 97) {
                int temp = (int) a[i];
                temp = temp - 32;
                newthing += str(temp);
            } else {
                int temp = (int) a[i];
                temp = temp + 32;
                newthing += str(temp);
                System.out.print(newthing);

            }
        }
    }
}