
#include "iostream"
using namespace std;

int main(void)
{

    class complex_num
    {
        public:

            complex_num(int Real_Num1 , int Img_Num1 , int Real_Num2 , int Img_Num2 )
            {
                cout << "The sum of real parts is: " << ( Real_Num1 + Real_Num2 ) << endl;

                cout << "The sum of imaginary parts is: " << ( Img_Num1 + Img_Num2 ) << endl;
            }
    };

    int RealNum1 , ImgNum1 , RealNum2 , ImgNum2 ;

    cout << "First number -> " << endl;
    
    cout << "Enter the real part: ";
    cin >> RealNum1;

    cout << "Enter the imaginary part: ";
    cin >> ImgNum1;

    cout << "Second number -> " << endl;
    
    cout << "Enter the real part: ";
    cin >> RealNum2;

    cout << "Enter the imaginary part: ";
    cin >> ImgNum2;

    complex_num cmplx_number_sum(RealNum1, ImgNum1, RealNum2, ImgNum2);

    return 0;
}