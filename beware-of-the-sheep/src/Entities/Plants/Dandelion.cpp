#include "Dandelion.h"

namespace bots {

	Dandelion::Dandelion(World & world, const Point & position) :
		Plant(world, position)
	{
	}

	void Dandelion::action()
	{
		Plant::action();
		Plant::action();
		Plant::action();
	}

} // namespace bots
