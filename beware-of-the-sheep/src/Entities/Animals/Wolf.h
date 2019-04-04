#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Wolf :
		public Animal
	{
	public:
		Wolf(World & world, const Point & position);
		virtual ~Wolf() = default;
	protected:
		inline const char * getSymbol() const override { return "WF"; }
	private:

	};

} // namespace bots
