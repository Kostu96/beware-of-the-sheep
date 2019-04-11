#include "pch.h"
#include "Antelope.h"

namespace bots {

	Antelope::Antelope(World & world, const Point & position) :
		Animal(world, position, 4, 4)
	{
	}

	void Antelope::action()
	{
		int xdir = 0, ydir = 0;
		while (xdir == 0 && ydir == 0) {
			xdir = rand() % 3 - 1;
			ydir = rand() % 3 - 1;
		}

		move(2 * xdir, 2 * ydir);
	}

	void Antelope::collision(Entity & other)
	{
		Animal::collision(other);
		// TODO: rest
	}

} // namespace bots
