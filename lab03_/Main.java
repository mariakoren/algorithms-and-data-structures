import java.sql.SQLOutput;
import java.util.Random;
public class Main {
    public static void main(String[] arg){
//        int[] Array =new int[] {7,4,1,10,6,9,12,5};

        //int[] Array=generateRandomArray(10, 1000);

        int[] nn = new int[] {1000,2000,3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,15000};
//        QuickSort(Array, 0, Array.length-1);
//        SortowanieBabelkowe(Array, 0, Array.length-1);
//        QuickSort_edycja(Array, 0, Array.length-1);
        System.out.println("\nDane losowe");
        for (int n: nn){
            int[] A=generateRandomArray(n, 1000);
            int[] B;
            B=A;
            int[] C;
            C=A;
            long start= System.nanoTime();
            QuickSort(A, 0, A.length-1);
            long stop=System.nanoTime();
            long czas_qs = stop-start;
            long start2=System.nanoTime();
            QuickSort_edycja(B, 0, B.length-1);
            long stop2=System.nanoTime();
            long czas_ed=stop2-start2;
            long start3=System.nanoTime();
            SortowanieBabelkowe(A, 0,C.length-1);
            long stop3=System.nanoTime();
            long czas_b=stop3-start3;
            System.out.println("dla "+n+" liczb qs-normalny: "+czas_qs);
            System.out.println("dla "+n+" liczb qs-edytowany: "+czas_ed);
            System.out.println("dla "+n+" liczb sortowanie bąbelkowe: "+czas_b);

        }

        System.out.println("\nDane skrajnie. Juz posortowane rosnąco");
        for (int n: nn){
            int[] A=generateRandomArray(n, 1000);
            Sortowanie(A);
            int[] B;
            B=A;
            int[] C;
            C=A;
            long start= System.nanoTime();
            QuickSort(A, 0, A.length-1);
            long stop=System.nanoTime();
            long czas_qs = stop-start;
            long start2=System.nanoTime();
            QuickSort_edycja(B, 0, B.length-1);
            long stop2=System.nanoTime();
            long czas_ed=stop2-start2;
            long start3=System.nanoTime();
            SortowanieBabelkowe(A, 0,C.length-1);
            long stop3=System.nanoTime();
            long czas_b=stop3-start3;
            System.out.println("dla "+n+" liczb qs-normalny: "+czas_qs);
            System.out.println("dla "+n+" liczb qs-edytowany: "+czas_ed);
            System.out.println("dla "+n+" liczb sortowanie bąbelkowe: "+czas_b);
        }

        System.out.println("\nDane skrajnie. Juz posortowane malejąco");
        for (int n: nn){
            int[] A=generateRandomArray(n, 1000);
            SortowanieOdwrotne(A);
            int[] B;
            B=A;
            int[] C;
            C=A;
            long start= System.nanoTime();
            QuickSort(A, 0, A.length-1);
            long stop=System.nanoTime();
            long czas_qs = stop-start;
            long start2=System.nanoTime();
            QuickSort_edycja(B, 0, B.length-1);
            long stop2=System.nanoTime();
            long czas_ed=stop2-start2;
            long start3=System.nanoTime();
            SortowanieBabelkowe(A, 0,C.length-1);
            long stop3=System.nanoTime();
            long czas_b=stop3-start3;
            System.out.println("dla "+n+" liczb qs-normalny: "+czas_qs);
            System.out.println("dla "+n+" liczb qs-edytowany: "+czas_ed);
            System.out.println("dla "+n+" liczb sortowanie bąbelkowe: "+czas_b);
        }

//        PrintArray(Array);


    }

    public static void QuickSort( int[] A, int p, int r){
        if (p<r){
            int q;
            q=partition(A, p, r);
            QuickSort(A, p, q);
            QuickSort(A, q+1, r);

        }

    }
    public static int partition(int[] A, int p, int r){
        int x=A[r];
        int i=p-1;
        for (int j=p; j<r+1; j++){
            if(A[j]<=x){
                i++;
                int tmp;
                tmp=A[i];
                A[i]=A[j];
                A[j]=tmp;
            }

        }

        if (i<r){
            return i;
        } else{
            return i-1;
        }

    }

    public static void PrintArray(int[] array){
        for (int i=0; i< array.length; i++){
            System.out.println(array[i]);
        }
    }

    public static void QuickSort_edycja(int[] A, int p, int r){
        if(r-p+1>5){
            int q;
            q=partition(A, p, r);
            QuickSort_edycja(A, p, q);
            QuickSort_edycja(A, q+1, r);
        } else {
            SortowanieBabelkowe(A, p, r);
        }
    }

    public static void SortowanieBabelkowe(int[] A, int poczatek, int koniec){
        for(int i=poczatek; i<=koniec; i++){
            for(int j=poczatek; j<=koniec; j++){
                if(A[j]>A[i]){
                    int tmp=A[i];
                    A[i]=A[j];
                    A[j]=tmp;
                }
            }
        }

    }

    public static void Sortowanie(int[] A){
        for(int i=0; i<A.length; i++){
            for(int j=0; j<A.length ;j++){
                if(A[j]>A[i]){
                    int tmp=A[i];
                    A[i]=A[j];
                    A[j]=tmp;
                }
            }
        }

    }

    public static void SortowanieOdwrotne(int[] A){
        for(int i=0; i<A.length; i++){
            for(int j=0; j<A.length ;j++){
                if(A[j]>A[i]){
                    int tmp=A[i];
                    A[i]=A[j];
                    A[j]=tmp;
                }
            }
        }

    }

    public static int[] generateRandomArray(int size,  int max) {
        int[] arr = new int[size];
        Random rand = new Random();
        for (int i = 0; i < size; i++) {
            arr[i] = rand.nextInt(max);
        }
        return arr;
    }
}