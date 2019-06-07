Add your answers to the Algorithms exercises here.

## Exercise I

a) O(n^3 / n^2) ==> O(n)
Covering n^3 at a rate of n^2 will leave O(n)

b) O(n/2 _ n/2 _ n/2 + 9) ==> O((n/2)^3 + 9) ==> O(n)^3
After ignoring the constants, the function should have the shape of O(n)^3

c) O(n)
For each function call, the is one recursive function call until the base case.
Meaning the function will be called n times

## Exercise II

In reality, an egg would break from a very short height so it'd probably be smartest to start from the bottom and keep going up a floor. However, in a programming sense that's not the most efficient way to find something you're looking for. So let's say the landing area is super padded to keep the egg safe until close to terminal velocity. We'll ignore the physics of the situation, since it could easily be calculated and floor estimated.

If I were coding this, I would start with the halfway point of the building (floor 50 for n=100) and drop the egg from there to get the results. From there you could continue halfway points until you find the layer where the egg breaks but floor - 1 does not. So if you drop from the halfway point and the egg doesn't break, I'd move up to the next halfway point (floor 75 for n=100). If it breaks, then move to the halfway point (floor 63). Since you are dividing the available data points in half each step, you should find the floor within log(n) steps.
