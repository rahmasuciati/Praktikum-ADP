#include<iostream>
#include<cmath>
using namespace std;
float rata2, ragam, simpangan_baku, a, b, c, d ,e, f;

int main() {
    cout << "\n Nama : Rahma Suciati \n";
    cout << "\n Nim : 2310432006 \n";

    cout << "\n menghitung rata2, ragam, dan simpangan baku \n";

    cout << "a = ";
    cin >> a;
    cout << "b = ";
    cin >> b;
    cout << "c = ";
    cin >> c;
    cout << "d = ";
    cin >> d;
    cout << "e = ";
    cin >> e;
    cout << "f = ";
    cin >> f;

    rata2 = ((a+b+c+d+e+f)/6);
    ragam = ((a-rata2)*(a-rata2))+((b-rata2)*(b-rata2))+((c-rata2)*(c-rata2))+((d-rata2)*(d-rata2))+((e-rata2)*(e-rata2))+((f-rata2)*(f-rata2));
    simpangan_baku = sqrt(ragam)
    
    cout << "nilai rata2 = " << rata2 << endl;
    cout << "nilai ragam = " << ragam << endl;
    cout << "nilai simpangan baku = " << simpangan_baku << endl;
    
    


    
}