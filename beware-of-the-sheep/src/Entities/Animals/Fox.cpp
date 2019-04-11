#include "pch.h"
#include "Fox.h"

namespace bots {

	Fox::Fox(World & world, const Point & position) :
		Animal(world, position, 3, 7)
	{}

	void Fox::action()
	{
		// temp TODO: proper
		Animal::action();
	}

} // namespace bots
