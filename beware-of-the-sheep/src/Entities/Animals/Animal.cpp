#include "pch.h"
#include "Animal.h"
#include "Entities/Plants/Plant.h"

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

	void Animal::collision(Entity & other)
	{
		if (dynamic_cast<Plant *>(&other)) {
			other.kill();
		}
	}

} // namespace bots
