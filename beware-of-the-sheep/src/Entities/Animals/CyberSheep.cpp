#include "pch.h"
#include "CyberSheep.h"

namespace bots {

	CyberSheep::CyberSheep(World & world, const Point & position) :
		Animal(world, position, 11, 4)
	{}

	void CyberSheep::action()
	{
	}

	void CyberSheep::collision(const Entity & other)
	{
	}

} // namespace bots
