#include "Turtle.h"
#include <random>

namespace bots {

	Turtle::Turtle(World & world, const Point & position) :
		Animal(world, position, 2, 1)
	{}

	void Turtle::action()
	{
		int x = rand() % 4;
		if (x == 0)
			Animal::action();
	}

	void Turtle::collision(const Entity & other)
	{
	}

} // namespace bots
