#pragma once
#include "Entities/Entity.h"

namespace bots {

	/*!
		\brief	Class representing a plant
		\author	Konstanty Misiak
	*/
	class Plant :
		public Entity
	{
	public:
		Plant(World & world, const Point & position, unsigned int strength = 0);
		virtual ~Plant() = default;

		void action() override;
		void collision(const Entity & /*other*/) override {}
	private:

	};

} // namespace bots
