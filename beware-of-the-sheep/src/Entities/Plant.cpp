#include "Plant.h"

namespace bots {

	Plant::Plant(World & world, const Point & position, unsigned int strength) :
		Entity(world, position, strength)
	{}

	void Plant::action()
	{
	}

} // namespace bots
