#pragma once
#include "Plant.h"

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
	protected:
		inline const char * getSymbol() const override { return "HW"; }
	private:

	};

} // namespace bots
