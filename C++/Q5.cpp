
#include "iostream"
using namespace std;

#define X 3

int main(void)
{
    unsigned int i ;
    unsigned int arr[X];
    unsigned int sum = 0;

    for ( i = 0; i < X; i++)
    {
        cout << "Enter Number " << ( i + 1 )  << ": ";
        cin >> arr[i] ;
        sum += arr[i];
    }
    

    cout << "Avrage = " << ( sum / X ) ;

}

