import java.util.Scanner;

public class MatrixOprations {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of matrix (M): ");
        int M = sc.nextInt();

        int[][] A = new int[M][M];
        int[][] B = new int[M][M];
        int[][] sum = new int[M][M];
        int[][] diff = new int[M][M];
        int[][] product = new int[M][M];

        System.out.println("Enter elements of Matrix A:");
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                A[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter elements of Matrix B:");
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                B[i][j] = sc.nextInt();
            }
        }

        // Addition and Subtraction
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                sum[i][j] = A[i][j] + B[i][j];
                diff[i][j] = A[i][j] - B[i][j];
            }
        }

        // Multiplication
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                product[i][j] = 0;
                for (int k = 0; k < M; k++) {
                    product[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        System.out.println("Addition of matrices:");
        printMatrix(sum);

        System.out.println("Subtraction of matrices:");
        printMatrix(diff);

        System.out.println("Multiplication of matrices:");
        printMatrix(product);

        sc.close();
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}
