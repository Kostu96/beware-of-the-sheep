#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Sheep :
		public Animal
	{
	public:
		Sheep(World & world, const Point & position);
		virtual ~Sheep() = default;
	protected:
		inline const char * getSymbol() const override { return "SP"; }
	private:

	};

} // namespace bots
