#pragma once
#include "../Plant.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Belladona :
		public Plant
	{
	public:
		Belladona(World & world, const Point & position);
		virtual ~Belladona() = default;

		void collision(const Entity & other) override;
		void draw() const override;
	private:

	};

} // namespace bots
