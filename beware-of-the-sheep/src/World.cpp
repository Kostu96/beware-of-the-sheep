#include "World.h"
#include "Entities/Animals.h"
#include "Entities/Plants.h"
#include <iostream>
#include <algorithm>
#include <random>
#include <ctime>

namespace bots {

	World::World(unsigned int width, unsigned int height) :
		m_width(width), m_height(height),
		m_area(width, height)
	{
		srand(static_cast<unsigned int>(time(nullptr)));

		spawnEntity(Entity::Kind::Human, { 1, 1 });
		//spawnEntity(Entity::Kind::CyberSheep, { 15, 15 });

		spawnEntity(Entity::Kind::Antelope, { 3, 3 });
		spawnEntity(Entity::Kind::Bellandona, { 5, 5 });
		spawnEntity(Entity::Kind::Dandelion, { 7, 7 });
		spawnEntity(Entity::Kind::Fox, { 9, 9 });
		spawnEntity(Entity::Kind::Grass, { 11, 11 });
		spawnEntity(Entity::Kind::Guarana, { 13, 13 });
		spawnEntity(Entity::Kind::Hogweed, { 15, 15 });
		spawnEntity(Entity::Kind::Sheep, { 17, 17 });
		spawnEntity(Entity::Kind::Turtle, { 19, 19 });
		spawnEntity(Entity::Kind::Wolf, { 21, 21 });
	}

	World::~World()
	{
		for (auto & e : m_entities)
			delete e;
	}

	void World::simulate()
	{
		while (m_isRunning)
		{
			print();
			tick();
		}
	}

	// TODO: use template?
	void World::spawnEntity(Entity::Kind kind, Point position)
	{
		switch (kind) {
		case Entity::Kind::Antelope:
			m_entities.push_back(new Antelope(*this, position));
			break;
		case Entity::Kind::CyberSheep:
			m_entities.push_back(new CyberSheep(*this, position));
			break;
		case Entity::Kind::Fox:
			m_entities.push_back(new Fox(*this, position));
			break;
		case Entity::Kind::Human:
			m_entities.push_back(new Human(*this, position));
			break;
		case Entity::Kind::Sheep:
			m_entities.push_back(new Sheep(*this, position));
			break;
		case Entity::Kind::Turtle:
			m_entities.push_back(new Turtle(*this, position));
			break;
		case Entity::Kind::Wolf:
			m_entities.push_back(new Wolf(*this, position));
			break;
		case Entity::Kind::Bellandona:
			m_entities.push_back(new Belladona(*this, position));
			break;
		case Entity::Kind::Dandelion:
			m_entities.push_back(new Dandelion(*this, position));
			break;
		case Entity::Kind::Grass:
			m_entities.push_back(new Grass(*this, position));
			break;
		case Entity::Kind::Guarana:
			m_entities.push_back(new Guarana(*this, position));
			break;
		case Entity::Kind::Hogweed:
			m_entities.push_back(new Hogweed(*this, position));
			break;
		}
	}

	void World::tick()
	{
		std::sort(m_entities.begin(), m_entities.end(),
			[](const Entity * a, const Entity * b) -> bool {

			unsigned int aInit = a->getInitiative(), bInit = b->getInitiative();

			if (aInit != bInit)
				return a->getInitiative() < b->getInitiative();

			return a->getLifeTime() < b->getLifeTime();
		});

		std::size_t size = m_entities.size();
		for (std::size_t i = 0; i < size; ++i)
			if (m_entities[i]->isAlive())
				m_entities[i]->action();

		// TODO: the rest
	}

	void World::printLegend() const
	{
		std::cout << "Plants:           Animals:        Special:\n"
				  << "BD - Belladonna   AT - Antilope   HM - Human\n"
				  << "DN - Dandelion    FX - Fox        CP - CyberSheep\n"
				  << "GS - Grass        SP - Sheep\n"
				  << "GA - Guarana      TT - Turtle\n"
				  << "HW - Hogweed      WF - Wolf";
	}

	void World::printSpacer() const
	{
		std::cout << "\n=================================================\n";
	}

	void World::print()
	{
		std::system("cls");
		std::cout << "Kontanty Misiak 175524\n";
		printSpacer();
		printLegend();
		printSpacer();

		m_area.clear();
		for (const auto & e : m_entities)
			e->draw(m_area);
		m_area.print();
		printSpacer();
	}

} // namepace bots
