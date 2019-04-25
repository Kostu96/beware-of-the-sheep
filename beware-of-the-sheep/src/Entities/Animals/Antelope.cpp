#include "pch.h"
#include "Antelope.h"
#include "World.h"

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
		int x = rand() % 2;
		if (x == 0)
			Animal::collision(other);
		else {
			Area::NeighboursArray arr{};
			unsigned int count = m_world.getFreeSpaceAround(getPosition(), arr);
			Point d = arr[rand() % count];
			move(d.x - getPosition().x, d.y - getPosition().y);
		}
	}

} // namespace bots
