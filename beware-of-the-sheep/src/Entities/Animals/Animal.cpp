#include "Animal.h"

namespace bots {

	Animal::Animal(World & world, const Point & position, unsigned int strength, unsigned int initiative) :
		Entity(world, position, strength, initiative)
	{}

	void Animal::action()
	{
	}

	void Animal::collision(const Entity & other)
	{
	}

} // namespace bots
