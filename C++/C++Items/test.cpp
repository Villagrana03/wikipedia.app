// #include <iostream>
// #include <string>

// int main() {
  
//   std::string pesos;
//   std::string reais;
//   std::string soles;
//   double dollar;

//   std::cout << "Enter number of Colombian Pesos: ";
//   std::cin >> pesos;
//   //std::cout << pesos << std::endl; here just printed the value of sol
//   std::cout << "Enter number of Brazilian Reais: ";
//   std::cin >> reais;
//   std::cout << "Enter number of Peruvian Soles:: ";
//   std::cin >> soles;
//   //std::cout << "Your Colombian pesos are: " << pesos << " Your reais are: " << reais << " And your soles are: " << soles;
//   int intPesos = std::stoi(pesos);
//   int intReais = std::stoi(reais);
//   int inSoles = std::stoi(soles);
  
//   //0.18 reaias = 1 dollar
//   //0.000236 peso = 1 dollar
//   // 0.27 sol = 1 dollar

//   dollar = (0.18 * intReais) + (0.000236 * intPesos) + (0.27 + inSoles);

//   std::cout << "Your total dollar is: " << dollar;
  
// }

#include <iostream>

int main(){
  char choice;
  do {
 

    std::cout << "Enter your choice (A/S/E): ";
    std::cin >> choice;

    if (choice == "A" || choice == "a") {
        std::cout << "\nAdd Book";
    } else if (choice == "S" || choice == "s") {
        std::cout << "\nSearch Book";
    } else if (choice != "E" && choice != "e") {
        std::cout << "\nInvalid input. Please try again.";
    }
} while (choice != "E" && choice != "e");
}