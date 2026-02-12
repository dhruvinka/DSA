import java.util.*;

class Hotel {

  String name;
  long mo_number;
  double salary;
  double bill_of_food,bill_of_room;
  int i, n;
  static int c=0,x=0;
  //static double Final_food_bill=0;
  String new_password;
  Scanner sc = new Scanner(System.in);

  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    Hotel h = new Hotel(5);

    Hotel a[] = new Hotel[7];
    Hotel f[] = new Hotel[10];
    a[0] = new Hotel();
    a[1] = new Hotel();
    a[2] = new Hotel();
    a[3] = new Hotel();
    a[4] = new Hotel();
    a[5] = new Hotel();
    a[6] = new Hotel();
	for(int i=0;i<10;i++)
	{
		f[i]=new Hotel();
		
	}
    a[0].name = "ankit bhayani chef";
    a[0].mo_number = 9574315467L;
    a[0].salary = 20000;
    a[1].name = "sanjay gujjar";
    a[1].salary = 18000;
    a[1].mo_number = 8934592751L;
    a[2].name = "tejas shah";
    a[2].salary = 21500;
    a[2].mo_number = 9163459769L;
	a[3].name = "jatin modi";
    a[3].salary = 30500;
    a[3].mo_number = 9846923419L;
	a[4].name = "jeni luise ";
    a[4].salary = 25000;
    a[4].mo_number = 9265425781L;
	a[5].name = "ruhi pandya";
    a[5].salary = 20500;
    a[5].mo_number = 8467928446L;
	a[6].name = "tejasbhai shah";
    a[6].salary = 50000;
    a[6].mo_number = 9967483187L;

    h.management(a,h,f);
  }

  Hotel( int a) {
    System.out.println("Welcome to hotel taj ");
	
  }

  void management(Hotel[] a, Hotel h, Hotel[] f) {
    f[i] = new Hotel();
    while (true) {
      Scanner sc = new Scanner(System.in);
      System.out.println("\nWhat would you like to do  ");
      System.out.println("1 : Know more about our hotel ");
      System.out.println("2 : Know more about our employees ");
      System.out.println("3 : Change employees details");
      System.out.println("4 : Room booking");
      System.out.println("5 : Room details ");
      System.out.println("6 : What would you like to eat ? ");
      System.out.println("7 : Todays total revenue");
      System.out.println("8 : Quit ");
      int choise = sc.nextInt();

      switch (choise) {
        case 1:
          {
            info();
            break;
          }
        case 2:
          {
            boolean dd1 = true;
            int count = 0;
            while (dd1) {
              sc.nextLine();
              System.out.println("enter password");
              new_password = sc.nextLine();
              if ((new_password).equals("LJU999")) {
                for (int i = 0; i < 7; i++) {
                  a[i].printData();
                }

                dd1 = false;
                break;
              } else {
                System.out.println("not matched try again");
                count++;
                if (count == 3) {
                  System.out.println("your system will be lock for 10 minutes");
                  break;
                }
              }
            }
            break;
          }
        case 3:
          {
			  change_details(a);
            break;
          }
        case 4:
          {
            Booking(f);
            break;
          }
        case 5:
          {
			  Room_details();
            break;
          }
        case 6:
          {
            boolean bb;
            for (i = 0; i < 3; i++) {
              bb = true;

              while (bb) {
                System.out.println();
                System.out.println("Enter Order of Room Number " + (i + 1));
                System.out.println();
                System.out.println("STARTERS\n");
                System.out.println("1.Hot & sour Soup ----------------200");
                System.out.println("2.Tomato soup---------------------200");
                System.out.println("3.Chili panner--------------------300");
                System.out.println("4.Pasta---------------------------250");
                System.out.println("5.Cheese bole---------------------300");
                System.out.println("\nMAIN COURCE\n");
                System.out.println("6.Panjabi sabji(kaju masala)------500");
                System.out.println("7.paneer haandi-------------------450");
                System.out.println("8.cheese butter masala------------600");
                System.out.println("9.naan----------------------------150");
                System.out.println("10.rumali roti--------------------100");
                System.out.println("11.butter chapati-----------------50");
                System.out.println("12.Jeera Rice---------------------300");
                System.out.println("13.Dal Fry------------------------250");
                System.out.println("\nDRINKS\n");
                System.out.println("14.Maaza--------------------------40");
                System.out.println("15.thums up-----------------------40");
                System.out.println("16.sprite-------------------------40");
                System.out.println("17.Butter milk--------------------50");
                System.out.println("\nDESSERTS\n");
                System.out.println("18.brownie------------------------150");
                System.out.println("19.Ice Cream(american dryfruites)-150");
                System.out.println("20.Cocolate Ice Cream-------------150");
                System.out.println("21.Donuts-------------------------200");
                System.out.println("22.Strawberry Ice Cream-----------150");
                System.out.println("23.special kulfi------------------100");
                System.out.println("24.Exit----------------");
                System.out.println("Enter Your Choice");
                int ch = sc.nextInt();
                if (ch == 24) {
                  bb = false;
                }
                if (ch != 24) {
                  System.out.println("Enter number quantity");
                  n = sc.nextInt();
                }
                h.CustomerFood(ch, n, i, f);
              }
            }
            break;
          }
		  case 7 :
		  {
			  finalFoodBill(f);
			  break;
		  }
        case 8:
          System.out.println("Goodbye!");
          return;
        default:
          System.out.println("\nInvalid choice. Please try again.");
          break;
      }
    }
  }

  Hotel() {}

  void info()
  {
	   System.out.println("Taj skyline is a chain of luxury hotels and a subsidiary of the Indian Hotels Company Limited");
	   System.out.println("Founded	 : 1902; 121 years ago");
	   System.out.println("Founder	 : Jamsetji Tata");
	   System.out.println("Services : Hotels and resorts");
	   System.out.println("Address  : The Taj Skyline, Sindhu Bhavan Marg, PRL Colony, Thaltej, Ahmedabad, Gujarat 380058");
	   
	  
  }

  void printData() {
	  x++;
    System.out.println("Employee "+x+" name=" + name);
    System.out.println("Employee "+x+" salary=" + salary);
    System.out.println("Employee "+x+" mobile number=" + mo_number);
  }

  void finalFoodBill(Hotel[] f) {
   double Total_food_bill=0,Total_room_bill=0;
    for (int i = 0; i < 10; i++) {
      Total_food_bill += f[i].bill_of_food;
	  Total_room_bill+=f[i].bill_of_room;
    }
	System.out.println("Todays total food revenue is "+Total_food_bill);
	System.out.println("Todays total room revenue is "+Total_room_bill);
	System.out.println("Todays total  revenue is "+(Total_food_bill+Total_room_bill));
  }

  void CustomerFood(int ch, int n, int i, Hotel[] f) {
    switch (ch) {
      case 1:
        {
          f[i].bill_of_food += (200 * n);
          System.out.println("Your Bill is :" + f[i].bill_of_food);
          System.out.println("hello");
          break;
        }
      case 2:
        {
          f[i].bill_of_food += (200 * n);
          System.out.println("Your Bill is :" + f[i].bill_of_food);
          break;
        }
      case 3:
        {
          f[i].bill_of_food += (300 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 4:
        {
          f[i].bill_of_food += (250 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 5:
        {
          f[i].bill_of_food += (300 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 6:
        {
          f[i].bill_of_food += (500 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 7:
        {
          f[i].bill_of_food += (450 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 8:
        {
          f[i].bill_of_food += (600 * n);
          System.out.println("Your Bill is" + f[i].bill_of_food);
          break;
        }
      case 9:
        {
          f[i].bill_of_food += (150 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 10:
        {
          f[i].bill_of_food += (100 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 11:
        {
          f[i].bill_of_food += (50 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 12:
        {
          f[i].bill_of_food += (300 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 13:
        {
          f[i].bill_of_food += (250 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 14:
        {
          f[i].bill_of_food += (40 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 15:
        {
          f[i].bill_of_food += (40 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 16:
        {
          f[i].bill_of_food += (40 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 17:
        {
          f[i].bill_of_food += (50 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 18:
        {
          f[i].bill_of_food += (150 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 19:
        {
          f[i].bill_of_food += (150 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 20:
        {
          f[i].bill_of_food += (150 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 21:
        {
          f[i].bill_of_food += (200 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 22:
        {
          f[i].bill_of_food += (150 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 23:
        {
          f[i].bill_of_food += (100 * n);
          System.out.println("Your Bill is:" + f[i].bill_of_food);
          break;
        }
      case 24:
        {
          System.out.println("Thank you!");
          return;
        }
      default:
        {
          System.out.println("Enter A Valid Choice");
          break;
        }
    }
  }

  void Booking(Hotel[] f) {
	  if(c==9)
	  {
		 System.out.println("Room is not available");
return;		 
	  }
	  
      System.out.println("\n***WELCOME TO OUR SUITS***\n");
      System.out.println("\nwe have one bad suits and two bad suits\n");
      System.out.println("1 : one bad");
      System.out.println("2 : two bad");
      System.out.println("3 : Exit");

      int n1 = sc.nextInt();
      switch (n1) {
		  
        case 1:
          {
            System.out.println("\nwe have A.C. suits and NON A.C. suits\n");
            System.out.println("1 : A.C.");
            System.out.println("2 : NON A.C.");
            int nn1 = sc.nextInt();
            switch (nn1) {
              case 1:
                {
                  System.out.println(
                    "\none bad with A.C. price is 5000 for one day " );
                  f[c].bill_of_room += 5000;
                  c++;
                  break;
                }
              case 2:
                {
                  System.out.println(
                    "\none bad with NON A.C. price is 4500 for one day ");
                  f[c].bill_of_room += 4500;
                  c++;
                  break;
                }
            }
           break;
          }
        case 2:
          {
            System.out.println("\nwe have A.C. suits and NON A.C. suits\n");
            System.out.println("1 : A.C.");
            System.out.println("2 : NON A.C.");
            int nn1 = sc.nextInt();
            switch (nn1) {
              case 1:
                {
                  System.out.println(
                    "\ntwo bad with A.C. price is 8000 for one day " );
                  f[c].bill_of_room += 8000;
                  c++;
                  break;
                }
              case 2:
                {
                  System.out.println(
                    "\ntwo bad with NON A.C. price is 7500 for one day ");
                  f[c].bill_of_room += 7500;
                  c++;
                  break;
                }
            }
            break;
          }
        case 3:
          {
            System.out.println("Goodbye!");
            return;
          }
        default:
          System.out.println("\nInvalid choice. Please try again.");
          break;
      }
   
  }
  void Room_details()
  {
	  for(int i=1;i<=c;i++)
	  {
		   System.out.println("Room "+i+" is booked");
	  }
	    for(int i=c+1;i<=10;i++)
	  {
		   System.out.println("Room "+i+" is not booked");
	  }
  }
  
  void change_details(Hotel[] a)
  {
	  
	  boolean dd1 = true;
            int count = 0;
            while (dd1) {
             
              System.out.println("enter password");
              new_password = sc.nextLine();
              if ((new_password).equals("LJU999")) {
                
                  while(true)
		{
		System.out.println("what do you want to change?");
		System.out.println("1 : Employee Name");
		System.out.println("2 : Employee Salary");
		System.out.println("3 : Employee Mobile number");
		System.out.println("4 : quit");
		int c=sc.nextInt();
		switch(c)
		{
			case 1:
			{
			System.out.println("Which employee name  you want to change?");
			System.out.println("1 : Employee one");
			System.out.println("2 : Employee two");
			System.out.println("3 : Employee three");
			System.out.println("4 : Employee four");
			System.out.println("5 : Employee five");
			System.out.println("6 : Employee six");
			System.out.println("7 : Employee seven");
			System.out.println("8 : Quit");
			int n=sc.nextInt();
			switch(n)
			{
				case 1:
				{
					sc.nextLine();
					System.out.println("enter new name of "+n+" employee");
					a[0].name=sc.nextLine();
					break;
				}
				case 2:
				{
					sc.nextLine();
					System.out.println("enter new name of "+n+" employee");
					a[1].name=sc.nextLine();
					break;
				}
				case 3:
				{
					sc.nextLine();
					System.out.println("enter new name of "+n+" employee");
					a[2].name=sc.nextLine();
					break;
				}
				case 4:
				{
					sc.nextLine();
					System.out.println("enter new name of "+n+" employee");
					a[3].name=sc.nextLine();
					break;
				}
				case 5:
				{
					sc.nextLine();
					System.out.println("enter new name of "+n+" employee");
					a[4].name=sc.nextLine();
					break;
				}
				case 6:
				{
					sc.nextLine();
					System.out.println("enter new name of "+n+" employee");
					a[5].name=sc.nextLine();
					break;
				}
				case 7:
				{
					sc.nextLine();
					System.out.println("enter new name of "+n+" employee");
					a[6].name=sc.nextLine();
					break;
				}
				case 8:
				{
                    System.out.println("Goodbye!");
					return;
				}
					default:
                    System.out.println("\nInvalid choice. Please try again.");
                    break;
			}
			break;
			}
			case 2:
			{
			System.out.println("Which employee salary  you want to change?");
			System.out.println("1 : Employee one");
			System.out.println("2 : Employee two");
			System.out.println("3 : Employee three");
			System.out.println("4 : Employee four");
			System.out.println("5 : Employee five");
			System.out.println("6 : Employee six");
			System.out.println("7 : Employee seven");
			System.out.println("8 : Quit");
			int s=sc.nextInt();
			switch(s)
			{
				case 1:
				{
					sc.nextLine();
					System.out.println("enter new salary of "+s+" employee");
					a[0].salary=sc.nextDouble();
					break;
				}
				case 2:
				{
					sc.nextLine();
					System.out.println("enter new salary of "+s+" employee");
					a[1].salary=sc.nextDouble();
					break;
				}
				case 3:
				{
					sc.nextLine();
					System.out.println("enter new salary of "+s+" employee");
					a[2].salary=sc.nextDouble();
					break;
				}
				case 4:
				{
					sc.nextLine();
					System.out.println("enter new salary of "+s+" employee");
					a[3].salary=sc.nextDouble();
					break;
				}
				case 5:
				{
					sc.nextLine();
					System.out.println("enter new salary of "+s+" employee");
					a[4].salary=sc.nextDouble();
					break;
				}
				case 6:
				{
					sc.nextLine();
					System.out.println("enter new salary of "+s+" employee");
					a[5].salary=sc.nextDouble();
					break;
				}
				case 7:
				{
					sc.nextLine();
					System.out.println("enter new salary of "+s+" employee");
					a[6].salary=sc.nextDouble();
					break;
				}
				case 8:
				{
                    System.out.println("Goodbye!");
					return;
				}
					default:
                    System.out.println("\nInvalid choice. Please try again.");
                    break;
			}break;
			}
			case 3:
			{
			System.out.println("Which employee mobile number you want to change?");
			System.out.println("1 : Employee one");
			System.out.println("2 : Employee two");
			System.out.println("3 : Employee three");
			System.out.println("4 : Employee four");
			System.out.println("5 : Employee five");
			System.out.println("6 : Employee six");
			System.out.println("7 : Employee seven");
			System.out.println("8 : Quit");
			int m=sc.nextInt();
			switch(m)
			{
				case 1:
				{
					sc.nextLine();
					System.out.println("enter new mobile number of "+m+" employee");
					a[0].mo_number=sc.nextLong();
					break;
				}
				case 2:
				{
					sc.nextLine();
					System.out.println("enter new mobile number of "+m+" employee");
					a[1].mo_number=sc.nextLong();
					break;
				}
				case 3:
				{
					sc.nextLine();
					System.out.println("enter new mobile number of "+m+" employee");
					a[2].mo_number=sc.nextLong();
					break;
				}
				case 4:
				{
					sc.nextLine();
					System.out.println("enter new mobile number of "+m+" employee");
					a[3].mo_number=sc.nextLong();
					break;
				}
				case 5:
				{
					sc.nextLine();
					System.out.println("enter new mobile number of "+m+" employee");
					a[4].mo_number=sc.nextLong();
					break;
				}
				case 6:
				{
					sc.nextLine();
					System.out.println("enter new mobile number of "+m+" employee");
					a[5].mo_number=sc.nextLong();
					break;
				}
				case 7:
				{
					sc.nextLine();
					System.out.println("enter new mobile number of "+m+" employee");
					a[6].mo_number=sc.nextLong();
					break;
				}
				case 8:
				{
                    System.out.println("Goodbye!");
					return;
				}
					default:
                    System.out.println("\nInvalid choice. Please try again.");
                    break;
			}
			break;
			}
				case 4 :
				{
					System.out.println("Goodbye!");
					dd1 = false;
					return;
				}
				default:
                    System.out.println("\nInvalid choice. Please try again.");
                    break;
				
		} 
		
	}
}
            }
        }
    }