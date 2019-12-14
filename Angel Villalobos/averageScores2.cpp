#include <iostream>
using namespace std;

int main()
{
    int score[3];
    double grade,
           sum = 0;

    for(int i = 0; i < 3; i++)
    {
        cout << "Enter score  #" << (i + 1) << ": ";
        cin >> score[i];
        sum += score[i];
    }
    grade = sum / 3.0;

    if (grade < 50)
        cout << "FAIL" << endl;
    else
        cout << "PASS" << endl;

    return 0;
}
