#include "pch.h"
#include "Guarana.h"

namespace bots {

	Guarana::Guarana(World & world, const Point & position) :
		Plant(world, position)
	{}

	void Guarana::collision(Entity & other)
	{
		other.addStrength(3);
	}

} // namespace bots
