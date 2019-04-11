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

		void collision(const Entity & other) override;
	protected:
		inline const char * getSymbol() const override { return "GA"; }
		inline Kind getKind() const override { return Kind::Guarana; }
		inline const char * getClassName() const override { return "Guarana"; }
	private:

	};

} // namespace bots
