#include "pch.h"
#include "World.h"
#include "Entities/Animals.h"
#include "Entities/Plants.h"


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

	Entity::Ptr World::getEntityAt(unsigned int x, unsigned int y)
	{
		auto found = std::find_if(m_entities.begin(), m_entities.end(),
			[x, y](const Entity::Ptr e) -> bool {
			return e->getPosition().x == x && e->getPosition().y == y;
		});

		return (found != m_entities.end() ? *found : nullptr);
	}

	void World::removeKilledEntites()
	{
		m_entities.erase(
			std::remove_if(
				m_entities.begin(),
				m_entities.end(),
				[](const Entity::Ptr e) -> bool {
					return !e->isAlive();
				}
			),
			m_entities.end()
		);
	}

	void World::sortEntities()
	{
		std::sort(m_entities.begin(), m_entities.end(),
			[](const Entity::Ptr a, const Entity::Ptr b) -> bool {

			unsigned int aInit = a->getInitiative(), bInit = b->getInitiative();

			if (aInit != bInit)
				return a->getInitiative() < b->getInitiative();

			return a->getLifeTime() < b->getLifeTime();
		});
	}

	void World::spawnEntity(Entity::Kind kind, Point position)
	{
		switch (kind) {
		case Entity::Kind::Antelope:
			m_entities.push_back(std::make_shared<Antelope>(*this, position));
			break;
		case Entity::Kind::CyberSheep:
			m_entities.push_back(std::make_shared <CyberSheep>(*this, position));
			break;
		case Entity::Kind::Fox:
			m_entities.push_back(std::make_shared<Fox>(*this, position));
			break;
		case Entity::Kind::Human:
			m_entities.push_back(std::make_shared<Human>(*this, position));
			break;
		case Entity::Kind::Sheep:
			m_entities.push_back(std::make_shared<Sheep>(*this, position));
			break;
		case Entity::Kind::Turtle:
			m_entities.push_back(std::make_shared<Turtle>(*this, position));
			break;
		case Entity::Kind::Wolf:
			m_entities.push_back(std::make_shared<Wolf>(*this, position));
			break;
		case Entity::Kind::Bellandona:
			m_entities.push_back(std::make_shared<Belladona>(*this, position));
			break;
		case Entity::Kind::Dandelion:
			m_entities.push_back(std::make_shared<Dandelion>(*this, position));
			break;
		case Entity::Kind::Grass:
			m_entities.push_back(std::make_shared<Grass>(*this, position));
			break;
		case Entity::Kind::Guarana:
			m_entities.push_back(std::make_shared<Guarana>(*this, position));
			break;
		case Entity::Kind::Hogweed:
			m_entities.push_back(std::make_shared<Hogweed>(*this, position));
			break;
		}
	}

	void World::tick()
	{
		removeKilledEntites();
		sortEntities();

		std::size_t size = m_entities.size();
		for (std::size_t i = 0; i < size; ++i)
			if (m_entities[i]->isAlive()) {
				m_entities[i]->action();
				const Point & position = m_entities[i]->getPosition();
				auto e = getEntityAt(position.x, position.y);
				if (e) {
					m_entities[i]->collision(*e);
					e->collision(*m_entities[i]);
				}
				m_entities[i]->incrementLifeTime();
			}
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
	}

} // namepace bots
