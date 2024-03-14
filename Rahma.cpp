#include<iostream>
using namespace std;

int main() {
    float jari2, volume, luas_permukaan;

    cout << "\n Nama : Rahma Suciati \n";
    cout << "\n Nim : 2310432006 \n";

    cout << "\n menghitung volume dan luas permukaan bola \n";

    cout << "input jari2 bola = ";
    cin >> jari2;

    volume = 4*(22/7)*jari2*jari2;
    luas_permukaan = (4/3)*(22/7)*jari2*jari2*jari2;

    cout << "volume bola = " << volume << endl;
    cout << "luas permukaan bola = "  << luas_permukaan << endl;


    return 0;
}