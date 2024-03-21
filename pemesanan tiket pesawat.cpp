#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main(){
char tujuan, kelas;
int nama, umur, jenis_kelamin, jumlah_kursi, beli, total, harga, bayar, kembali;
printf("TRANSAKSI PEMBELIAN TIKET PESAWAT\n");
printf("Nama          : Rahma Suciati\n");
printf("Umur          : 18 tahun\n");
printf("jenis kelamin : perempuan\n");
cout<<"_________________________________________\n";
cout<<"Tujuan yang dipilih:\n1.Jakarta\n2.Bandung\n3.Aceh\n";
cin>>tujuan;
if (tujuan==1){"Jakarta";}
else if (tujuan==2){"Bandung";}
else if (tujuan==3){"Aceh";}
else {
      "error";
}
cout<<"_________________________________________\n";
cout<<"kelas yang dipilih:\n1.Ekonomi\n2.Bisnis\n3.First class\n";
cin>>kelas;
if (kelas==1){
    harga=1000000;
    "Ekonomi";
}
else if (kelas==2){
        harga=1500000;
        "Bisnis";
}
else if(tujuan==3){
       harga=2000000;
       "First class";
}
else {
      "error";
}

cout<<"__________________________________________\n";
cout<<"Jumlah kursi : ";
cin>>beli;
cout<<"__________________________________________\n";

if (beli > 3){
   "diskon 0.25";
}
else {
     "tidak ada diskon";
}     
total = beli*harga;
cin>>total;
cout<<"__________________________________________\n";
cout<<"Tujuan                 : "<<tujuan<<endl;
cout<<"Kelas                  : "<<kelas<<endl;
cout<<"Harga                  : "<<harga<<endl;
cout<<"Jumlah kursi           : "<<beli<<endl;
cout<<"Total                  : "<<total<<endl<<endl;

printf("\tPEMBAYARAN\n");
cout<<"_________________________________________\n";
cout<<"Uang bayar : ";
cin>>bayar;
kembali=bayar-total;
cout<<"Uang kembali : "<<kembali<<endl<<endl;
cout<<"______________TERIMAKASIH_________________\n"<<endl<<endl;

return 0;
}

   
