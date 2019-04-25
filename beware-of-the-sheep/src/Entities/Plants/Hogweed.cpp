#include "pch.h"
#include "Hogweed.h"
#include "Entities/Animals/CyberSheep.h"
#include "World.h"

namespace bots {

	Hogweed::Hogweed(World & world, const Point & position) :
		Plant(world, position)
	{}

	void Hogweed::action()
	{
		long lxpos = static_cast<long>(getPosition().x), lypos = static_cast<long>(getPosition().y);
		unsigned int xpos = getPosition().x, ypos = getPosition().y;
		unsigned int width = m_world.getWidth(), height = m_world.getHeight();

		unsigned int nx = (lxpos - 1 < 0 ? lxpos - 1 + width : (lxpos - 1) % width);
		auto e = m_world.getEntityAt(nx, ypos);
		if (dynamic_cast<Animal*>(e.get()) && e->getKind() != Entity::Kind::Hogweed && e->getKind() != Entity::Kind::CyberSheep)
			e->kill();

		nx = (lxpos + 1 < 0 ? lxpos + 1 + width : (lxpos + 1) % width);
		e = m_world.getEntityAt(nx, ypos);
		if (dynamic_cast<Animal*>(e.get()) && e->getKind() != Entity::Kind::Hogweed && e->getKind() != Entity::Kind::CyberSheep)
			e->kill();

		unsigned int ny = (lypos - 1 < 0 ? lypos - 1 + height : (lypos - 1) % height);
		e = m_world.getEntityAt(xpos, ny);
		if (dynamic_cast<Animal*>(e.get()) && e->getKind() != Entity::Kind::Hogweed && e->getKind() != Entity::Kind::CyberSheep)
			e->kill();

		ny = (lypos + 1 < 0 ? lypos + 1 + height : (lypos + 1) % height);
		e = m_world.getEntityAt(xpos, ny);
		if (dynamic_cast<Animal*>(e.get()) && e->getKind() != Entity::Kind::Hogweed && e->getKind() != Entity::Kind::CyberSheep)
			e->kill();

		Plant::action();
	}

	void Hogweed::collision(Entity & other)
	{
		if (!dynamic_cast<CyberSheep *>(&other))
			other.kill();
	}

} // namespace bots
