#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Turtle :
		public Animal
	{
	public:
		Turtle(World & world, const Point & position);
		virtual ~Turtle() = default;

		void action() override;
		void collision(const Entity & other) override;
	protected:
		inline const char * getSymbol() const override { return "TT"; }
	private:

	};

} // namespace bots
