#include "pch.h"
#include "Fox.h"
#include "World.h"

namespace bots {

	Fox::Fox(World & world, const Point & position) :
		Animal(world, position, 3, 7)
	{}

	void Fox::action()
	{
		Point dir[4]{};
		unsigned int count = 0;

		long lxpos = static_cast<long>(getPosition().x), lypos = static_cast<long>(getPosition().y);
		unsigned int xpos = getPosition().x, ypos = getPosition().y;
		unsigned int width = m_world.getWidth(), height = m_world.getHeight();

		unsigned int nx = (lxpos - 1 < 0 ? lxpos - 1 + width : (lxpos - 1) % width);
		auto e = m_world.getEntityAt(nx, ypos);
		if (!e || e->getStrength() < getStrength())
			dir[count++] = { nx, ypos };

		nx = (lxpos + 1 < 0 ? lxpos + 1 + width : (lxpos + 1) % width);
		e = m_world.getEntityAt(nx, ypos);
		if (!e || e->getStrength() < getStrength())
			dir[count++] = { nx, ypos };

		unsigned int ny = (lypos - 1 < 0 ? lypos - 1 + height : (lypos - 1) % height);
		e = m_world.getEntityAt(nx, ypos);
		if (!e || e->getStrength() < getStrength())
			dir[count++] = { xpos, ny };

		ny = (lypos + 1 < 0 ? lypos + 1 + height : (lypos + 1) % height);
		e = m_world.getEntityAt(nx, ypos);
		if (!e || e->getStrength() < getStrength())
			dir[count++] = { xpos, ny };

		Point d = dir[rand() % count];
		move(d.x - xpos, d.y - ypos);
	}

} // namespace bots
