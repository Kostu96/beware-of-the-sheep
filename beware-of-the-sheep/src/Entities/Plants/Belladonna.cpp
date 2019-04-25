#include "pch.h"
#include "Belladonna.h"
#include "World.h"
#include "Entities/Animals/Animal.h"

namespace bots {

	Belladona::Belladona(World & world, const Point & position) :
		Plant(world, position, 99)
	{}

	void Belladona::collision(Entity & other)
	{
		if (dynamic_cast<Animal *>(&other)) {
			if (other.getStrength() < getStrength())
				other.kill();
			std::string message = other.getClassName() + " was slain by " + getClassName();
			m_world.addMessage(std::move(message));
		}
	}

} // namespace bots
