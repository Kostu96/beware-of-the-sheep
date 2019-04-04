#include "World.h"
#include "Entities/Animals.h"
#include "Entities/Plants.h"
#include <iostream>

namespace bots {

	World::World(unsigned int width, unsigned int height) :
		m_width(width), m_height(height),
		m_area(width, height)
	{
		m_entities.push_back(new Antelope(*this, { 1, 2 }));
	}

	World::~World()
	{
		for (auto & e : m_entities)
			delete e;
	}

	void World::simulate()
	{
		while (true)
		{
			m_area.clear();

			for (const auto & e : m_entities)
				e->draw(m_area);

			m_area.print();

			std::cin.get();
		}
	}

} // namepace bots
