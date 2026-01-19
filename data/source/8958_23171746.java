import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for(int i = 0; i < tc; i++) {
            int ans = 0;
            int cnt = 0;
            String s = sc.next();
            for(int j = 0; j < s.length(); j++) {
                if(s.charAt(j) == 'O') {
                    cnt++;
                }
                else {
                    cnt = 0;
                }
                ans += cnt;
            }
            System.out.println(ans);
        }
    }
}