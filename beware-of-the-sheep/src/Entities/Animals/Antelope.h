#pragma once
#include "../Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Antelope :
		public Animal
	{
	public:
		Antelope(World & world, const Point & position);
		virtual ~Antelope() = default;

		void action() override;
		void collision(const Entity & other) override;
		void draw() const override;
	private:

	};

} // namespace bots
