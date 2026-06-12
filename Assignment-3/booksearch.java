import java.util.ArrayList;
import java.util.Scanner;

public class BookSearch
{
    public static void main(String[] args)
    {
        ArrayList<String> books = new ArrayList<>();

        // Add at least 5 books
        books.add("Introduction to Algorithms");
        books.add("Java Programming");
        books.add("Data Structures");
        books.add("Artificial Intelligence");
        books.add("Computer Networks");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a word to search: ");
        String word = sc.nextLine();

        System.out.println("\nMatching books:");

        boolean found = false;

        for (String title : books)
        {
            if (title.toLowerCase().contains(word.toLowerCase()))
            {
                System.out.println(title);
                found = true;
            }
        }

        if (!found)
        {
            System.out.println("No matching books found.");
        }

        sc.close();
    }
}
