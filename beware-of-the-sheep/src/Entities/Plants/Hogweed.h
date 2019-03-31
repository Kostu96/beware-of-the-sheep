#pragma once
#include "../Plant.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Hogweed :
		public Plant
	{
	public:
		Hogweed(World & world, const Point & position);
		virtual ~Hogweed() = default;

		void action() override;
		void collision(const Entity & other) override;
		void draw() const override;
	private:

	};

} // namespace bots
