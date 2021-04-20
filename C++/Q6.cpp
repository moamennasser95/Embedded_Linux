
#include "iostream"
using namespace std;

int main(void)
{

    class int_sum
    {
        public:

            int_sum(int N1 , int N2 )
            {
                cout << "Numbers initialized." << endl;

                cout << "The addition result is: " << ( N1 + N2 ) << endl;
            }
    };

    int Num1, Num2 ;

    cout << "Enter first number : ";

    cin >> Num1 ;

    cout << "Enter second number : ";

    cin >> Num2 ;

    int_sum two_numbers( Num1 , Num2 );

    return 0;
}