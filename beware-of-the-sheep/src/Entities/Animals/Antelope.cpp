#include "Antelope.h"

namespace bots {

	Antelope::Antelope(World & world, const Point & position) :
		Animal(world, position, 4, 4)
	{
	}

	void Antelope::action()
	{
	}

	void Antelope::collision(const Entity & other)
	{
	}

	void Antelope::draw() const
	{
	}

} // namespace bots
