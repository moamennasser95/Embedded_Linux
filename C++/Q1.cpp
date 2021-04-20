
#include "iostream"
using namespace std;

int main(void)
{
	
    int num;

    cout << "Enter your favorite number between 1 and 100: ";
    
    cin >> num;

    if(num >= 1 && num <= 100)
    {
        cout << "Amazing!! That's my favorite number too!" << endl;
        cout << "No really!! " << num << " is my favorite number!" << endl;
    }
    else
    {
        cout << "Sorry but this isn't my favorite number" << endl;
    }
    
    return 0;
}