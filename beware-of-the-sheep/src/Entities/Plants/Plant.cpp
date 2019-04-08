#include "Plant.h"
#include <random>
#include "../../World.h"
#include <iostream>

// TODO: precompiled header

namespace bots {

	Plant::Plant(World & world, const Point & position, unsigned int strength) :
		Entity(world, position, strength)
	{}

	void Plant::action()
	{
		int c = rand() % 8;
		if (c == 0) {
			int x = 0, y = 0;
			while (x == 0 && y == 0) {
				x = rand() % 3 - 1;
				y = rand() % 3 - 1;
			}
			m_world.requestSpawn(Entity::Kind::Grass, { getPosition().x + x, getPosition().y + y });
		}
	}

} // namespace bots
