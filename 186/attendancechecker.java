import java.util.*;
public class attendancechecker {

	public static void main(String[] args) {
		

		// Create a list of students
        List<Student> students = new ArrayList<>();
        students.add(new Student("ABINES,PRINCESS ")); 
        students.add(new Student("ARTUBAL, JEDY"));
        students.add(new Student("BAURA, SUGAR "));
        students.add(new Student("BONTIA, DARLYN"));
        students.add(new Student("CERVANTES, JAMES"));
        students.add(new Student("DAMILES, KYLA"));
        students.add(new Student("DEOGRACIAS, ZENREB"));
        students.add(new Student("DIJOS, MARIE"));
        students.add(new Student("DUMAPIAS, JAY"));
        students.add(new Student("EBESA , KLARENCE"));
     
     
        Scanner scanner = new Scanner(System.in);

        while (true) {
            // Display main menu
            System.out.println("Main Menu:");
            System.out.println("--------------------------\n");
            System.out.println("1. Add attendance");
            System.out.println("2. View attendance report");
            System.out.println("3. Exit");
            System.out.println("--------------------------");
            System.out.println("Select number: ");
            

            // Get user input
            int choice = 0;
            try {
                choice = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a valid integer.");
                scanner.next();
                continue;
            }

            // Process user choice
            if (choice == 1) {
                // Add attendance
                scanner.nextLine(); // Consume newline
                System.out.print("Enter date (MM/DD/YYYY): ");
                String date = scanner.nextLine();

                System.out.println(" (P for present and A for absent): ");
                for (Student student : students) {
                    System.out.print(student.getName() + " : ");

                    String status = scanner.next().toUpperCase();
                    while (!status.equals("P") && !status.equals("A")) {
                        System.out.print("Invalid input. Please enter P for present or A for absent: ");
                        status = scanner.next().toUpperCase();
                    }
                    student.recordAttendance(date, status);
                }
                scanner.nextLine(); // Consume newline
                System.out.println("Attendance added successfully.");

            } else if (choice == 2) {
                // View attendance report
                System.out.println("Attendance Report:");
                System.out.println("--------------------------------------------------------");
                System.out.printf("%-20s%-20s%-20s%n", "Name", "Present", "Absent");
                System.out.println("--------------------------------------------------------");
                for (Student student : students) {
                    int presentCount = 0;
                    int absentCount = 0;
                    for (String status : student.getAttendance().values()) {
                        if (status.equals("P")) {
                            presentCount++;
                        } else if (status.equals("A")) {
                            absentCount++;
                        }
                    }
                    System.out.printf("%-20s%-20d%-20d%n", student.getName(), presentCount, absentCount);
                }
                System.out.println("--------------------------------------------------------");

            } else if (choice == 3) {
                // Exit
                System.out.println("Exiting program...");
                break;

            } else {
                System.out.println("Invalid input. Please enter a valid choice.");
            }
        }
    }
}

class Student {
    private String name;
    private Map<String, String> attendance;

    public Student(String name) {
        this.name = name;
        this.attendance = new HashMap<>();
    }

    public String getName() {
        return this.name;
    }

    public void recordAttendance(String date, String status) {
        attendance.put(date, status);
    }

    public Map<String, String> getAttendance() {
        return attendance;
    }
}