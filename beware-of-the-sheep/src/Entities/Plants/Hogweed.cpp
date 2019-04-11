#include "pch.h"
#include "Hogweed.h"
#include "Entities/Animals/CyberSheep.h"

namespace bots {

	Hogweed::Hogweed(World & world, const Point & position) :
		Plant(world, position)
	{}

	void Hogweed::action()
	{
	}

	void Hogweed::collision(Entity & other)
	{
		if (!dynamic_cast<CyberSheep *>(&other))
			other.kill();
	}

} // namespace bots
