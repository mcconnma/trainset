#include <iostream>
#include <time.h>
using namespace std;

// Swap function 
void SWAP(int &a, int &b)
{

    int temp;
    temp=a;
    a=b;
    b=temp;
}

void perm(int *array, int start, int end, int &count)
{
    // If we have reached the last two numbers by swapping
    // then just print the whole array, swap the last 2 numbers
    // and print the array once again
    if((end-start) == 1)
    {

        for(int i=0;i<=end;i++)
            cout << array[i] << " - ";
        cout << endl;

        SWAP(array[start],array[end]);

        for(int i=0;i <= end;i++)
            cout << array[i] << " - ";
        cout << endl << endl;

        // Swap it back to restore the order of the numbers
        SWAP(array[start],array[end]);
        count =2;

    }
    else
    {

        for(int i=start;i <=end;i++ )
        {

            // Bring a number at the front
            SWAP(array[i],array[start]);

            // Call the permuation function on th sub array
            // formed by leaving out the first number
            perm(array,start+1,end,count);

            // Swap back the number to restore the order of the
            // numbers in the array
            SWAP(array[i],array[start]);

        }
    }
}
int main()
{
    srand(time(NULL));
    int len;
    cout << "Enter the number of elements" << endl;
    cin>>len;
    int array[len];
    cout << "enter the numbers" << endl;
    for(int i=0;i<len;i++)
        cin>>array[i];

    int count=0;
    perm(array,0,len-1,count);
    cout << endl << "Total number of permutations are " << count << endl;

    system("pause");
    return 0;
}
