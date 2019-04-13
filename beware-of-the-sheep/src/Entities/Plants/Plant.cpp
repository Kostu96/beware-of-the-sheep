#include "pch.h"
#include "Plant.h"
#include "World.h"

namespace bots {

	Plant::Plant(World & world, const Point & position, unsigned int strength) :
		Entity(world, position, strength)
	{}

	void Plant::action()
	{
		Area::NeighboursArray arr{};
		unsigned int count = m_world.getFreeSpaceAround(getPosition(), arr);
		
		int c = rand() % 40;
		if (c == 0 && count > 0) {
			m_world.spawnEntity(getKind(), arr[rand() % count]);

		}
	}

} // namespace bots
