
#include "iostream"
using namespace std;

int main(void)
{

    int num; 

    cout << "Enter an integer: ";

    cin >> num;

    cout << "Reversed number = ";

    while(num != 0)   
    {
        cout << num % 10;

        num /= 10;
    }

    cout << endl;

    return 0;
    
}