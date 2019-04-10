#include "Animal.h"
#include <random>

namespace bots {

	Animal::Animal(World & world, const Point & position, unsigned int strength, unsigned int initiative) :
		Entity(world, position, strength, initiative)
	{}

	void Animal::action()
	{
		int vorh, norp;
		vorh = rand() % 2;
		norp = rand() % 2;
		
		if (vorh)
			move(0, norp ? -1 : 1);
		else
			move(norp ? -1 : 1, 0);
	}

	void Animal::collision(const Entity & other)
	{
	}

} // namespace bots
