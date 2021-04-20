
#include "iostream"
using namespace std;

#define X 5

int main(void)
{
    unsigned int i , max = 0 ;

    unsigned int arr[X];

    for(i = 0 ; i < X ; i++)
    {
        cout << "Enter number " << (i + 1) << " : ";
        
        cin >> arr[i];

        if(max < arr[i])
        {   
            max = arr[i];
        }

    }

    cout << "Largest element = " << max << endl;

    return 0;
}