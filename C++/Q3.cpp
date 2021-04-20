
#include "iostream"
using namespace std;

#define X 5

int main(void)
{
    int arr[X] ;

    int *ptr ;

    int i ;

    cout << "Enter elements: " << endl;

    for(i = 0 ; i < X ; i++)
    {
        cin >> arr[i];
    }
    
    ptr = arr;

    cout << "You entered: " << endl;

    for(i = 0 ; i < X ; i++)
    {   
        cout << *(ptr+i) << endl;
    }

    return 0;
}