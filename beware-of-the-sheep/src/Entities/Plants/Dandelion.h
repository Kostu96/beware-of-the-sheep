#pragma once
#include "Plant.h"

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
	protected:
		inline const char * getSymbol() const override { return "DN"; }
	private:

	};

} // namespace bots
