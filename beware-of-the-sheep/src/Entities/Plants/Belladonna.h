#pragma once
#include "Plant.h"

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
	protected:
		inline const char * getSymbol() const override { return "BD"; }
		inline Kind getKind() const override { return Kind::Bellandona; }
	private:

	};

} // namespace bots
