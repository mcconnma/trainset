The purpose of this post is to explore and discover the number of permutations of a childrens 16 piece train track set.
The trainset of interest is the following:

![alt text](http://mcconnma.github.io/trainset/lillabo-trainset.jpg)


This particular trainset has a total of 16 track piecies, 12 curved and 4 straight. The curved pieces are reversible (the straight ones are not) and 2 of the 4 straight pieces form a bridge as in the picture. I am interested in all solutions, for example those that use 10 or 12 pieces, not just all 16. Additionally, I want to solve this programatically and to create a visual representation of the solutions. A solution will be presented that uses Python to solve it programatically, along with a 2d graphics program called Cairo.

First, we need to determine if we are talking about permutations or combinantions? In the case of building a solution for a trainset, in which the order of the tracks does matter, we are talking about permutations without repetitions. In that case, the general formula for the number of permutations is the following:

n!/(n−r)!
Where n is the number of choices, in our case 16 for number of tracks, and r is how many are chosen from the set. For example, the minimilist solution would be a circle, in which 8 pieces are used. So, in order to find the one and only solution of 8 pieces, we would need to check the following number of permutations:

16!/(8)!=518,918,400


# Permutations of a childrens traiset
http://mcconnma.github.io/posts/trainset-p1/
