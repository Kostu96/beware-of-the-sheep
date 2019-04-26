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

		void collision(Entity & other) override;
	protected:
		inline std::string getSymbol() const override { return "BD"; }
		inline Kind getKind() const override { return Kind::Bellandona; }
		inline std::string getClassName() const override { return "Belladonna"; }
	private:

	};

} // namespace bots
