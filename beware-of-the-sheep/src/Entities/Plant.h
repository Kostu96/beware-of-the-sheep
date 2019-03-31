#pragma once
#include "Entity.h"

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
	private:

	};

} // namespace bots
