#include "pch.h"
#include "Guarana.h"
#include "World.h"

namespace bots {

	Guarana::Guarana(World & world, const Point & position) :
		Plant(world, position)
	{}

	void Guarana::collision(Entity & other)
	{
		other.addStrength(3);
		std::string message = other.getClassName() + " has now " + std::to_string(other.getStrength()) + " Strength";
		m_world.addMessage(std::move(message));
	}

} // namespace bots
