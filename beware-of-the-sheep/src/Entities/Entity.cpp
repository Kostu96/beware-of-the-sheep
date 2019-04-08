#include "Entity.h"
#include "../World.h"
#include "../Area.h"

namespace bots {

	Entity::Entity(World & world, const Point & position, unsigned int strength, unsigned int initiative) :
		m_world(world),
		m_position(position),
		m_strength(strength),
		m_initiative(initiative)
	{
		m_position.x %= m_world.getWidth();
		m_position.y %= m_world.getHeight();
	}

	void Entity::draw(Area & area) const
	{
		area.put(m_position, getSymbol());
	}

	void Entity::move(int x, int y)
	{
		long newX = m_position.x + x;
		newX %= m_world.getWidth();
		m_position.x = static_cast<unsigned int>(newX);

		long newY = m_position.y + y;
		newY %= m_world.getHeight();
		m_position.y = static_cast<unsigned int>(newY);
	}

} // namespace bots
