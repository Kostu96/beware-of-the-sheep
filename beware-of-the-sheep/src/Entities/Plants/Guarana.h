#pragma once
#include "../Plant.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Guarana :
		public Plant
	{
	public:
		Guarana(World & world, const Point & position);
		virtual ~Guarana() = default;

		void collision(const Entity & other) override;
		void draw() const override;
	private:

	};

} // namespace bots
