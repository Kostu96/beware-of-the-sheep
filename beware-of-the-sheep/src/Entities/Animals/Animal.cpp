#include "Animal.h"
#include <random>

namespace bots {

	Animal::Animal(World & world, const Point & position, unsigned int strength, unsigned int initiative) :
		Entity(world, position, strength, initiative)
	{}

	void Animal::action()
	{
		int xdir = 0, ydir = 0;
		while (xdir == 0 && ydir == 0) {
			xdir = rand() % 3 - 1;
			ydir = rand() % 3 - 1;
		}

		move(xdir, ydir);
	}

	void Animal::collision(const Entity & other)
	{
	}

} // namespace bots
