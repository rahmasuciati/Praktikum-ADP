#include<iostream>
using namespace std;
int main (){
    int rows;
    char alphabet='A';
    printf("PIRAMIDA ALPHABET\n");
    printf("===================================\n");
    cout<<"masukkan jumlah huruf pada pitamida : ";
    cin>>rows;
    for(int i=1;i<=rows;i++){
        for(int space=1;space<=rows-i;space++){
            cout<< " ";
        }
        
        for(int j=1;j<=2*i-1;j++){
            cout<<alphabet;
            if(j<i){
               alphabet++;
            }
            else{
               alphabet--;
            }
        }
        alphabet++;
        cout<<endl;              
    }
    
    return 0;
    }