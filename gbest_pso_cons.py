#########################################################################################################################
#Global Best Particle Optimization
#Problem: Take an integer as input from a user between -300 to 300 (inclusive). Find a combination of 3 numbers that, 
#when added, yields the user's number. These 3 numbers must also be in the range -300 to 300 (inclusive)
#inertia weight = 0.5, r1 & r2 = random numbers between 0 and 1 (exclusive) from a uniform distribution, c1 = c2 = 0.49
#THIS ONE ALSO MAKES USE OF THE CONSTRICTION FACTOR k
#########################################################################################################################
import math, random;

def fitness (particle, target):
	return (abs(sum (particle) - target));

def gbest_pso (swarm, target):
	r1, r2, c1, c2 = random.random (), random.random (), 3, 3;
	fitnesses = {i : (fitness (swarm [i], target), swarm [i], 0) for i in range (len (swarm)) };
	velocities = { i : [0 for j in range (len (swarm [0]))] for i in range (len (swarm)) }
	iterations, phi = 0, c1 + c2;
	k = (2 * random.random ()) / abs (2 - phi - math.sqrt ( (phi ** 2) - (4 * phi) ));

#	print (k);
#	for i in velocities: print (i, velocities [i]);
#	for i in fitnesses: print (i, fitnesses [i]);

	while (min (fitnesses.values ()) [0] > 0 and iterations < 5000):
		iterations += 1;
#		print (min (fitnesses.values ()));
		for key in fitnesses:
			if (fitnesses [key] [0] > fitness (swarm [key], target)):
				fitnesses [key] = (fitness (swarm [key], target), swarm [key]);

		for i in range (len (swarm)):
			for dimen in range (len (swarm [i])):
				velocities [i] [dimen] = k * ( (velocities [i] [dimen]) + (random.random () * c1 * (fitnesses [i] [1] [dimen] - swarm [i] [dimen])) + (random.random () * c2 * (min (fitnesses.values ()) [1] [dimen] - swarm [i] [dimen])) );
				swarm [i] [dimen] += velocities [i] [dimen];

	return (min (fitnesses.values ()) [1]);

def main ():
	swarm, target = [], int (input ('Enter target value (range: -300 to 300 inclusive): '));
	while (len (swarm) < 25):
		particle = [random.randint (-100, 100) for i in range (3)];
		if (not particle in swarm):
			swarm.append (particle);

#	print ('The randomly generated Swarm Population is: ');
#	for particle in swarm: print ('%d\t%d\t%d' % (particle [0], particle [1], particle [2]));

	optimal = gbest_pso (swarm, target)
	print ('The retrieved optimal values are %d, %d and %d\nSum: %d' % (optimal [0], optimal [1], optimal [2], optimal [0] + optimal [1] + optimal [2]));

if (__name__ == '__main__'):
	main ();
