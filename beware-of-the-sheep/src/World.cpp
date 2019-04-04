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
			print();

			std::cin.get();
		}
	}

	void World::print()
	{
		std::system("cls");
		std::cout << "Kontanty Misiak 175524\n\n";

		m_area.clear();

		for (const auto & e : m_entities)
			e->draw(m_area);

		m_area.print();
	}

} // namepace bots
