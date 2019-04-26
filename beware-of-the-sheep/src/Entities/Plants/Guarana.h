#pragma once
#include "Plant.h"

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

		void collision(Entity & other) override;
	protected:
		inline std::string getSymbol() const override { return "GA"; }
		inline Kind getKind() const override { return Kind::Guarana; }
		inline std::string getClassName() const override { return "Guarana"; }
	private:

	};

} // namespace bots
