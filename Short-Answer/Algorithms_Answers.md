#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This example is O(log(n)) because as the size of N grows it takes longer for a to catch up to n * n * n. However the time that a takes to catch up to N is also directly corelated to how large N is.


b) This example would be O(n^2) because as N grows, it increases both the iterations of the for loop as well as the while loop


c)This example would be O(n) because as the number of bunnies increase, the number of iterations increase at the same rate.

## Exercise II


I would approach this problem with a middle variable, start at the middle floor, if it drops and breaks, move down one floor, otherwise move up. if moving down, once the egg doesnt break, thats the highest floor, if moving up, once the egg breaks the floor below is the highest floor.
