#include <iostream>

#include <stdlib.h>

using namespace std;

void output(int string[], int position);

void generate(int string[], int position, int positions);

int length;

// This function takes "string", which contains a description

// of what bits should be set in the output, and writes the

// corresponding binary representation to the terminal.

// The variable "position" is the effective last position.

void
output(int string[], int position)

{

int * temp_string = new int[length];

int index = 0;

int i;

for (i = 0; i < length; i++)

{

if ((index < position) && (string[index] == i))

{

temp_string[i] = 1;

index++;

}

else

temp_string[i] = 0;

}

for (i = 0; i < length; i++)

cout << temp_string[i];

delete [] temp_string;

cout << endl;

}

// Recursively generate the banker's sequence.

void
generate(int string[], int position, int positions)

{

if (position < positions)

{

if (position == 0)

{

for (int i = 0; i < length; i++)

{

string[position] = i;

generate(string, position + 1, positions);

}

}

else

{

for (int i = string[position - 1] + 1; i < length; i++)

{

string[position] = i;

generate(string, position + 1, positions);

}

}

}

else

output(string, positions);

}

// Main program accepts one parameter: the number of elements

// in the set. It loops over the allowed number of ones, from

// zero to n.

int
main (int argc, char ** argv)

{

if (argc != 2)

{

cout << "Usage: " << argv[0] << " n" << endl;

exit(1);

}

length = atoi(argv[1]);

for (int i = 0; i <= length; i++)

{

int * string = new int[length];

generate(string, 0, i);

delete [] string;

}

return (0);

}

