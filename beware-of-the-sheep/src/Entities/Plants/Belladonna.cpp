#include "pch.h"
#include "Belladonna.h"

namespace bots {

	Belladona::Belladona(World & world, const Point & position) :
		Plant(world, position, 99)
	{}

	void Belladona::collision(const Entity & other)
	{
	}

} // namespace bots
