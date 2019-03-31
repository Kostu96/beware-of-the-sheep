#pragma once
#include "../Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Fox :
		public Animal
	{
	public:
		Fox(World & world, const Point & position);
		virtual ~Fox() = default;

		void action() override;
		void draw() const override;
	private:

	};

} // namespace bots
