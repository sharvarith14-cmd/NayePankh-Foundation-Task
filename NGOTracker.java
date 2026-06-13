import java.util.HashMap;
import java.util.Scanner;

public class NGOTracker {
    public static void main(String[] args) {
        // Data store karne ke liye HashMap (Donor Name -> Donation Amount)
        HashMap<String, Double> donationDB = new HashMap<>();
        Scanner scanner = new Scanner(System.in);
        
        // Pehle se kuch dummy data add kar dete hain
        donationDB.put("Amit Sharma", 5000.0);
        donationDB.put("Priya Patel", 2500.0);
        donationDB.put("Rohan Das", 1500.0);

        while (true) {
            System.out.println("\n=== NayePankh Foundation - Java Resource Tracker ===");
            System.out.println("1. Add New Donation");
            System.out.println("2. Search Donor Details");
            System.out.println("3. Generate Total Donation Report");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            
            int choice = scanner.nextInt();
            scanner.nextLine(); // newline character clear karne ke liye

            if (choice == 1) {
                System.out.print("Enter Donor Name: ");
                String name = scanner.nextLine();
                System.out.print("Enter Donation Amount (INR): ");
                double amount = scanner.nextDouble();
                
                donationDB.put(name, amount);
                System.out.println("🎉 Donation recorded successfully for " + name + "!");
                
            } else if (choice == 2) {
                System.out.print("Enter Donor Name to Search: ");
                String searchName = scanner.nextLine();
                if (donationDB.containsKey(searchName)) {
                    System.out.println("🔍 Found: " + searchName + " donated ₹" + donationDB.get(searchName));
                } else {
                    System.out.println("❌ No record found for " + searchName);
                }
                
            } else if (choice == 3) {
                System.out.println("\n--- 📋 NGO DONATION REPORT ---");
                double total = 0;
                for (String donor : donationDB.keySet()) {
                    System.out.println("- " + donor + ": ₹" + donationDB.get(donor));
                    total += donationDB.get(donor);
                }
                System.out.println("-----------------------------");
                System.out.println("💰 Total Funds Collected: ₹" + total);
                
            } else if (choice == 4) {
                System.out.println("Thank you for supporting NayePankh Foundation! Goodbye.");
                break;
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        }
        scanner.close();
    }
}
