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
		m_position.x += x;
		m_position.x %= m_world.getWidth();
		m_position.y += y;
		m_position.y %= m_world.getHeight();
	}

} // namespace bots
