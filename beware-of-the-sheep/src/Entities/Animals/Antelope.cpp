#include "pch.h"
#include "Antelope.h"

namespace bots {

	Antelope::Antelope(World & world, const Point & position) :
		Animal(world, position, 4, 4)
	{
	}

	void Antelope::action()
	{
		int vorh, norp;
		vorh = rand() % 2;
		norp = rand() % 2;

		if (vorh)
			move(0, norp ? -2 : 2);
		else
			move(norp ? -2 : 2, 0);
	}

	void Antelope::collision(Entity & other)
	{
		Animal::collision(other);
		// TODO: rest
	}

} // namespace bots
