import java.util.*;

// Base Class
class Account {
    private String accountNumber;
    private String ownerName;
    private double balance;

    // Constructor chaining
    public Account() {
        this("000", "Unknown", 0.0);
    }

    public Account(String accNo, String name, double bal) {
        this.accountNumber = accNo;
        this.ownerName = name;
        setBalance(bal);
    }

    // Getters & Setters
    public double getBalance() { return balance; }

    public void setBalance(double bal) {
        if (bal < 0) throw new IllegalArgumentException("Negative balance");
        this.balance = bal;
    }

    // Core methods
    public void deposit(double amt) {
        if (amt <= 0) throw new IllegalArgumentException("Invalid deposit");
        balance += amt;
    }

    public void withdraw(double amt) {
        if (amt <= 0 || amt > balance)
            throw new IllegalArgumentException("Invalid withdraw");
        balance -= amt;
    }

    public void display() {
        System.out.println(accountNumber + " | " + ownerName + " | " + balance);
    }
}

// SavingsAccount
class SavingsAccount extends Account {
    private double interestRate;

    public SavingsAccount(String a, String n, double b, double r) {
        super(a, n, b);
        this.interestRate = r;
    }

    double interest() {
        return getBalance() * interestRate / 100;
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Interest: " + interest());
    }
}

// CurrentAccount
class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount(String a, String n, double b, double l) {
        super(a, n, b);
        this.overdraftLimit = l;
    }

    @Override
    public void withdraw(double amt) {
        if (amt <= 0 || amt > getBalance() + overdraftLimit)
            throw new IllegalArgumentException("Overdraft exceeded");
        setBalance(getBalance() - amt);
    }

    @Override
    public void display() {
        super.display();
        System.out.println("OD Limit: " + overdraftLimit);
    }
}

// Main (Polymorphism)
public class Main {
    public static void main(String[] args) {
        List<Account> list = new ArrayList<>();

        list.add(new SavingsAccount("S1", "A", 1000, 5));
        list.add(new CurrentAccount("C1", "B", 2000, 500));

        for (Account acc : list)
            acc.display();   // polymorphism
    }
}