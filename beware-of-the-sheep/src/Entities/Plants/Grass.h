#pragma once
#include "../Plant.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Grass :
		public Plant
	{
	public:
		Grass(World & world, const Point & position);
		virtual ~Grass() = default;

		void draw() const override;
	private:

	};

} // namespace bots
