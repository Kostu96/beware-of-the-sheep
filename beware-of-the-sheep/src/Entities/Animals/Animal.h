#pragma once
#include "Entities/Entity.h"

namespace bots {

	/*!
		\brief	Class representing an animal
		\author	Konstanty Misiak
	*/
	class Animal :
		public Entity
	{
	public:
		Animal(World & world, const Point & position, unsigned int strength, unsigned int initiative);
		virtual ~Animal() = default;

		void action() override;
		void collision(Entity & other) override;
	private:

	};

} // namespace bots
