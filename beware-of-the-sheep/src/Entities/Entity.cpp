#include "Entity.h"
#include "../World.h"

namespace bots {

	Entity::Entity(World & world, const Point & position, unsigned int strength, unsigned int initiative) :
		m_world(world),
		m_position(position),
		m_strength(strength),
		m_initiative(initiative)
	{}

	void Entity::move(unsigned int x, unsigned int y)
	{
		m_position.x += x;
		m_position.x %= m_world.getSizeX();
		m_position.y += y;
		m_position.y %= m_world.getSizeY();
	}

} // namespace bots
