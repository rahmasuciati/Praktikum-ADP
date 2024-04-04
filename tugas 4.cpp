#include<iostream>
using namespace std;

int main() {
    int total_angka = 100;
    int angka_per_baris = 10;
    int angka = 1;
    
    for (int i = 0; i < total_angka; i++){
          if (angka % 5 == 0){
              cout << "DOR";
           }   
           else if (angka % 3 == 0){
                    cout << "DOR";
           }
           else {
                cout << angka << " ";  
           }
             
           if ((i + 1) % angka_per_baris == 0){
               cout << endl;
           } 
           
           angka++;
   }
              
return 0;
}
 
    