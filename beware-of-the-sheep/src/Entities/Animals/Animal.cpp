#include "pch.h"
#include "Animal.h"
#include "Entities/Plants/Plant.h"
#include "World.h"

namespace bots {

	Animal::Animal(World & world, const Point & position, unsigned int strength, unsigned int initiative) :
		Entity(world, position, strength, initiative)
	{}

	void Animal::action()
	{
		int vorh, norp;
		vorh = rand() % 2;
		norp = rand() % 2;
		
		if (vorh)
			move(0, norp ? -1 : 1);
		else
			move(norp ? -1 : 1, 0);
	}

	void Animal::collision(Entity & other)
	{
		std::string message;
		if (dynamic_cast<Plant*>(&other)) {
			other.kill();
			message = other.getClassName() + " was eaten by " + getClassName();
			m_world.addMessage(std::move(message));
			other.collision(*this);
		}
		else if (getKind() == other.getKind()) {
			moveToPrevPosition();
			Area::NeighboursArray arr{};
			unsigned int count = m_world.getFreeSpaceAround(getPosition(), arr);

			if (count > 0)
				m_world.spawnEntity(getKind(), arr[rand() % count]);
		}
		else if (other.dodgedAttack())
			moveToPrevPosition();
		if (other.getStrength() <= getStrength()) {
			other.kill();
			message = other.getClassName() + " was slain by " + getClassName();
			m_world.addMessage(std::move(message));
		}
		else {
			kill();
			message = getClassName() + " was slain by " + other.getClassName();
			m_world.addMessage(std::move(message));
		}
	}

} // namespace bots
