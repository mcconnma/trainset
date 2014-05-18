#include <stdio.h>

/* function to swap array elements */

void swap (int v[], int i, int j) {
	int	t;

	t = v[i];
	v[i] = v[j];
	v[j] = t;
}

/* recursive function to generate permutations */
void perm (int v[], int n, int i) {

	/* this function generates the permutations of the array
	 * from element i to element n-1
	 */
	int	j;

	/* if we are at the end of the array, we have one permutation
	 * we can use (here we print it; you could as easily hand the
	 * array off to some other function that uses it for something
	 */
	if (i == n) {
		for (j=0; j<n; j++) printf ("%d ", v[j]);
		printf ("\n");
	} else
		/* recursively explore the permutations starting
		 * at index i going through index n-1
		 */
		for (j=i; j<n; j++) {

			/* try the array with i and j switched */

			swap (v, i, j);
			perm (v, n, i+1);

			/* swap them back the way they were */

			swap (v, i, j);
		}
}
			
/* little driver function to print perms of first 5 integers */

int main () {
	int	v[5], i;

	for (i=0; i<5; i++) v[i] = i+1;
	v[1] = 1;
	v[2] = 1;
	v[4] = 2;
	perm (v, 5, 0);
	exit (0);
}
