#pragma once
#include "../Plant.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Dandelion :
		public Plant
	{
	public:
		Dandelion(World & world, const Point & position);
		virtual ~Dandelion() = default;

		void action() override;
		void draw() const override;
	private:

	};

} // namespace bots
