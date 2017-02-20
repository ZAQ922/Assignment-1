//This is just a basic outline of what the program should look like IMO. 

#include <iostream>
#include <iomain>
using namespace std;

int main(){
  //Variables go here
  int Input = 0;
  
  //User chooses which application to run
  cout << "Choose: /t1 = BMI /t2 = Retirement /t3 = Distance /t4 = Email" << endl;
  cin >> Input >> endl;
  
  //Put in while loop to handle things like "ctrl+c"?
  switch(Input){
    case '1'://BMI
      
      break;
    case '2'://Retirement
    
      break;
    case '3'://Distance
    
      break;
    case '4'://Email
      
      break;
    default://Any input I don't like = end program.
      cout << "Wrong Choice." << endl;
      return 0;
      break;
  }

  return 0;
}
